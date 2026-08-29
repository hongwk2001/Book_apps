package com.tkprof.shared.ui.reader

import android.app.Application
import android.media.AudioManager
import android.media.AudioFocusRequest
import android.content.Context
import android.os.Build

import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.tkprof.shared.billing.BillingManager
import com.tkprof.shared.data.BookRepository
import com.tkprof.shared.model.BilingualChapter
import com.tkprof.shared.model.BookConfig
import com.tkprof.shared.model.Language
import com.tkprof.shared.model.Sentence
import com.tkprof.shared.model.SentenceSplitter
import com.tkprof.shared.tts.TtsManager
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import android.content.Intent
import androidx.core.content.ContextCompat
import com.tkprof.shared.tts.TtsPlaybackService

class ReaderViewModel(
    application: Application,
    val bookConfig: BookConfig,
    val ttsManager: TtsManager,
    val billingManager: BillingManager
) : AndroidViewModel(application) {

    private val repository = BookRepository(application)

    private val prefs = application.getSharedPreferences("ReaderPrefs", Context.MODE_PRIVATE)


    private val _currentChapter = MutableStateFlow<BilingualChapter?>(null)
    val currentChapter: StateFlow<BilingualChapter?> = _currentChapter

    private val _currentChapterNumber = MutableStateFlow(1)
    val currentChapterNumber: StateFlow<Int> = _currentChapterNumber

    val fontSizeMultiplier = MutableStateFlow(1.0f)

    private val ttsReceiver = object : android.content.BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            when (intent?.action) {
                "com.tkprof.shared.TTS_PLAY" -> {
                    if (!ttsManager.isSpeaking.value) playOrPause()
                }
                "com.tkprof.shared.TTS_PAUSE" -> {
                    if (ttsManager.isSpeaking.value) playOrPause()
                }
                "com.tkprof.shared.TTS_NEXT" -> {
                    nextSentence()
                }
                "com.tkprof.shared.TTS_PREV" -> {
                    previousSentence()
                }
            }
        }
    }

    init {
        androidx.core.content.ContextCompat.registerReceiver(
            application,
            ttsReceiver,
            android.content.IntentFilter().apply {
                addAction("com.tkprof.shared.TTS_PLAY")
                addAction("com.tkprof.shared.TTS_PAUSE")
                addAction("com.tkprof.shared.TTS_NEXT")
                addAction("com.tkprof.shared.TTS_PREV")
            },
            androidx.core.content.ContextCompat.RECEIVER_NOT_EXPORTED
        )
    }
    
    override fun onCleared() {
        super.onCleared()
        try {
            getApplication<Application>().unregisterReceiver(ttsReceiver)
        } catch (e: Exception) {}
        ttsManager.shutdown()
        billingManager.disconnect()
    }


    private val _speakingSentenceId = MutableStateFlow<String?>(null)
    val speakingSentenceId: StateFlow<String?> = _speakingSentenceId

    private val _totalChapters = MutableStateFlow(bookConfig.totalChapters)
    val totalChapters: StateFlow<Int> = _totalChapters

    val isFullUnlocked: StateFlow<Boolean> = billingManager.isFullUnlocked
    val isSpeaking: StateFlow<Boolean> = ttsManager.isSpeaking

    
    private val audioManager = application.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var wasPlayingBeforeFocusLoss = false

    private val audioFocusChangeListener = AudioManager.OnAudioFocusChangeListener { focusChange ->
        when (focusChange) {
            AudioManager.AUDIOFOCUS_LOSS, AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
                if (isSpeaking.value) {
                    wasPlayingBeforeFocusLoss = true
                    ttsManager.stop()
                }
            }
            AudioManager.AUDIOFOCUS_GAIN -> {
                if (wasPlayingBeforeFocusLoss) {
                    wasPlayingBeforeFocusLoss = false
                    playCurrentSequence()
                }
            }
        }
    }

    private fun requestAudioFocus(): Boolean {
        val result = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val focusRequest = AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
                .setOnAudioFocusChangeListener(audioFocusChangeListener)
                .build()
            audioManager.requestAudioFocus(focusRequest)
        } else {
            @Suppress("DEPRECATION")
            audioManager.requestAudioFocus(
                audioFocusChangeListener,
                AudioManager.STREAM_MUSIC,
                AudioManager.AUDIOFOCUS_GAIN
            )
        }
        return result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
    }

    private val _speakingParagraphIndex = MutableStateFlow(-1)
    val speakingParagraphIndex: StateFlow<Int> = _speakingParagraphIndex

    // Settings States
    val isEnFirst = MutableStateFlow(true) // Language Order
    val showEn = MutableStateFlow(true)
    val showKo = MutableStateFlow(true)
    val readEn = MutableStateFlow(true)
    val readKo = MutableStateFlow(true)

    private val _bypassedUpToChapter = MutableStateFlow(0)
    val bypassedUpToChapter: StateFlow<Int> = _bypassedUpToChapter

    // Flat queue of all playable sentences in the chapter
    private var sentenceQueue = listOf<Sentence>()
    private var currentQueueIndex = -1

        init {
        val lastChapter = prefs.getInt("last_chapter", 1)
        val lastSentenceId = prefs.getString("last_sentence_id", null)
        _bypassedUpToChapter.value = prefs.getInt("bypassed_up_to_chapter", 0)
        loadChapter(lastChapter, lastSentenceId)
        
        viewModelScope.launch { _totalChapters.value = repository.availableChapterCount() }
        
        // Listen to TTS state to update the foreground service
        viewModelScope.launch {
            var hasStartedPlaying = false
            isSpeaking.collect { speaking ->
                if (speaking) hasStartedPlaying = true
                if (hasStartedPlaying) {
                    val intent = Intent(application, TtsPlaybackService::class.java).apply {
                        putExtra("BOOK_TITLE", bookConfig.titleEn)
                        putExtra("IS_PLAYING", speaking)
                    }
                    ContextCompat.startForegroundService(application, intent)
                }
            }
        }
        
        // Auto-save sentence progress
        viewModelScope.launch {
            speakingSentenceId.collect { id ->
                if (id != null) {
                    prefs.edit().putString("last_sentence_id", id).apply()
                }
            }
        }
    }

    fun loadChapter(number: Int, restoreSentenceId: String? = null, autoPlay: Boolean = false, playFromEnd: Boolean = false, selectOnLoad: Boolean = false) {
        prefs.edit().putInt("last_chapter", number).apply()
        viewModelScope.launch(Dispatchers.IO) {
            ttsManager.stop()
            _speakingSentenceId.value = null
            currentQueueIndex = -1
            _currentChapterNumber.value = number
            val ch = repository.loadChapter(number)
            _currentChapter.value = ch
            rebuildSentenceQueue(ch)
            
            if (restoreSentenceId != null) {
                val idx = sentenceQueue.indexOfFirst { it.id == restoreSentenceId }
                if (idx != -1) {
                    currentQueueIndex = idx
                    _speakingSentenceId.value = restoreSentenceId
                    _speakingParagraphIndex.value = ch?.paragraphs?.indexOfFirst { it.id == sentenceQueue[idx].paragraphId } ?: -1
                }
            } else {
                prefs.edit().remove("last_sentence_id").apply()
            }
            
            if ((autoPlay || selectOnLoad) && sentenceQueue.isNotEmpty()) {
                if (playFromEnd) {
                    var idx = sentenceQueue.size - 1
                    while (idx >= 0) {
                        val s = sentenceQueue[idx]
                        val shouldRead = if (s.lang == Language.EN) readEn.value else readKo.value
                        if (shouldRead) break
                        idx--
                    }
                    currentQueueIndex = if (idx >= 0) idx else sentenceQueue.size - 1
                } else {
                    currentQueueIndex = 0
                }
                playCurrentSequence(play = autoPlay)
            }
        }
    }

    private fun rebuildSentenceQueue(chapter: BilingualChapter?) {
        if (chapter == null) {
            sentenceQueue = emptyList()
            return
        }
        val queue = mutableListOf<Sentence>()
        for (paragraph in chapter.paragraphs) {
            
            val enSentences = SentenceSplitter.split(paragraph.en, Language.EN, paragraph.id)
            val koSentences = SentenceSplitter.split(paragraph.ko, Language.KO, paragraph.id)
            
            if (isEnFirst.value) {
                queue.addAll(enSentences)
                queue.addAll(koSentences)
            } else {
                queue.addAll(koSentences)
                queue.addAll(enSentences)
            }
        }
        sentenceQueue = queue
    }

    /** Rebuild queue when Language Order changes */
    fun updateLanguageOrder(enFirst: Boolean) {
        isEnFirst.value = enFirst
        rebuildSentenceQueue(_currentChapter.value)
    }

    fun nextChapter() {
        val next = _currentChapterNumber.value + 1
        if (next <= _totalChapters.value) loadChapter(next)
    }

    fun previousChapter() {
        val prev = _currentChapterNumber.value - 1
        if (prev >= 1) loadChapter(prev)
    }

    fun isChapterAccessible(chapterNumber: Int): Boolean = true

    fun shouldShowSoftPaywall(chapterNumber: Int): Boolean {
        if (billingManager.isFullUnlocked.value) return false
        return (chapterNumber % 3 == 0) && (_bypassedUpToChapter.value < chapterNumber)
    }

    fun bypassSoftPaywall() {
        val current = _currentChapterNumber.value
        prefs.edit().putInt("bypassed_up_to_chapter", current).apply()
        _bypassedUpToChapter.value = current
    }

    /** Start playing from a specific sentence */
    fun playFromSentence(sentenceId: String) {
        val index = sentenceQueue.indexOfFirst { it.id == sentenceId }
        if (index != -1) {
            currentQueueIndex = index
            playCurrentSequence()
        }
    }

    fun playOrPause() {
        if (isSpeaking.value) {
            wasPlayingBeforeFocusLoss = false
            ttsManager.stop()
            _speakingSentenceId.value = null
        } else {
            if (currentQueueIndex == -1 && sentenceQueue.isNotEmpty()) {
                currentQueueIndex = 0
            }
            if (currentQueueIndex in sentenceQueue.indices) {
                playCurrentSequence()
            }
        }
    }

    fun nextSentence() {
        ttsManager.stop()
        
        var tempIndex = currentQueueIndex + 1
        while (tempIndex < sentenceQueue.size) {
            val s = sentenceQueue[tempIndex]
            val shouldRead = if (s.lang == Language.EN) readEn.value else readKo.value
            if (shouldRead) break
            tempIndex++
        }

        if (tempIndex < sentenceQueue.size) {
            currentQueueIndex = tempIndex
            playCurrentSequence(play = false)
        } else {
            val next = _currentChapterNumber.value + 1
            if (next <= _totalChapters.value && isChapterAccessible(next)) {
                loadChapter(next, autoPlay = false, selectOnLoad = true)
            } else {
                _speakingSentenceId.value = null
            }
        }
    }

    fun previousSentence() {
        ttsManager.stop()
        
        var tempIndex = currentQueueIndex - 1
        while (tempIndex >= 0) {
            val s = sentenceQueue[tempIndex]
            val shouldRead = if (s.lang == Language.EN) readEn.value else readKo.value
            if (shouldRead) break
            tempIndex--
        }

        if (tempIndex >= 0) {
            currentQueueIndex = tempIndex
            playCurrentSequence(play = false)
        } else {
            val prev = _currentChapterNumber.value - 1
            if (prev >= 1) {
                loadChapter(prev, autoPlay = false, playFromEnd = true, selectOnLoad = true)
            } else {
                _speakingSentenceId.value = null
            }
        }
    }

    private fun playCurrentSequence(play: Boolean = true) {
        if (play && !requestAudioFocus()) return

        if (currentQueueIndex !in sentenceQueue.indices) {
            if (currentQueueIndex >= sentenceQueue.size && sentenceQueue.isNotEmpty()) {
                val next = _currentChapterNumber.value + 1
                if (next <= _totalChapters.value && isChapterAccessible(next)) {
                    loadChapter(next, autoPlay = play, selectOnLoad = !play)
                    return
                }
            }
            _speakingSentenceId.value = null
            _speakingParagraphIndex.value = -1
            return
        }
        
        val s = sentenceQueue[currentQueueIndex]
        
        // Update paragraph index for auto-scroll
        val ch = _currentChapter.value
        if (ch != null) {
            _speakingParagraphIndex.value = ch.paragraphs.indexOfFirst { it.id == s.paragraphId }
        }

        _speakingSentenceId.value = s.id
        
        if (!play) return
        
        // Check if we should read this language
        val shouldRead = if (s.lang == Language.EN) readEn.value else readKo.value
        
        if (!shouldRead) {
            // Skip and go to next
            currentQueueIndex++
            playCurrentSequence()
            return
        }

        _speakingSentenceId.value = s.id
        val onDone = {
            currentQueueIndex++
            playCurrentSequence()
        }

        if (s.lang == Language.EN) {
            ttsManager.speakEnglish(s.text, onDone)
        } else {
            ttsManager.speakKorean(s.text, onDone)
        }
    }

    fun stopSpeaking() {
        wasPlayingBeforeFocusLoss = false
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) {
            @Suppress("DEPRECATION")
            audioManager.abandonAudioFocus(audioFocusChangeListener)
        }
        ttsManager.stop()

        _speakingSentenceId.value = null
    }

}


