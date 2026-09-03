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
                    if (!isPlaying.value) playOrPause()
                }
                "com.tkprof.shared.TTS_PAUSE" -> {
                    if (isPlaying.value) playOrPause()
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
            val stopIntent = Intent(getApplication(), TtsPlaybackService::class.java).apply {
                action = "STOP_SERVICE"
            }
            getApplication<Application>().startService(stopIntent)
        } catch (e: Exception) {}
        ttsManager.shutdown()
        billingManager.disconnect()
    }


    private val _chapterTitles = MutableStateFlow<List<com.tkprof.shared.model.ChapterTitle>>(emptyList())
    val chapterTitles: StateFlow<List<com.tkprof.shared.model.ChapterTitle>> = _chapterTitles

    private val _speakingSentenceId = MutableStateFlow<String?>(null)
    val speakingSentenceId: StateFlow<String?> = _speakingSentenceId

    private val _totalChapters = MutableStateFlow(bookConfig.totalChapters)
    val totalChapters: StateFlow<Int> = _totalChapters

    val isFullUnlocked: StateFlow<Boolean> = billingManager.isFullUnlocked
    
    private val _isPlaying = MutableStateFlow(false)
    val isPlaying: StateFlow<Boolean> = _isPlaying

    val isSpeaking: StateFlow<Boolean> = ttsManager.isSpeaking

    
    private val audioManager = application.getSystemService(Context.AUDIO_SERVICE) as AudioManager
    private var wasPlayingBeforeFocusLoss = false

    private val audioFocusChangeListener = AudioManager.OnAudioFocusChangeListener { focusChange ->
        when (focusChange) {
            AudioManager.AUDIOFOCUS_LOSS, AudioManager.AUDIOFOCUS_LOSS_TRANSIENT -> {
                hasAudioFocus = false
                if (isPlaying.value) {
                    wasPlayingBeforeFocusLoss = true
                    _isPlaying.value = false
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

    private var hasAudioFocus = false
    private var focusRequestObj: Any? = null

    private fun requestAudioFocus(): Boolean {
        if (hasAudioFocus) return true
        val result = if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val request = (focusRequestObj as? android.media.AudioFocusRequest) ?: android.media.AudioFocusRequest.Builder(AudioManager.AUDIOFOCUS_GAIN)
                .setOnAudioFocusChangeListener(audioFocusChangeListener)
                .build().also { focusRequestObj = it }
            audioManager.requestAudioFocus(request)
        } else {
            @Suppress("DEPRECATION")
            audioManager.requestAudioFocus(
                audioFocusChangeListener,
                AudioManager.STREAM_MUSIC,
                AudioManager.AUDIOFOCUS_GAIN
            )
        }
        hasAudioFocus = result == AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        return hasAudioFocus
    }

    private val _speakingParagraphIndex = MutableStateFlow(-1)
    val speakingParagraphIndex: StateFlow<Int> = _speakingParagraphIndex

    // Settings States
    val languageOrder = MutableStateFlow(listOf(Language.EN, Language.KO))
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
        
        viewModelScope.launch(Dispatchers.IO) {
            val titles = repository.loadAllChapterTitles()
            _chapterTitles.value = titles
            _totalChapters.value = titles.size
        }
        
        // Immediately start TtsPlaybackService on ViewModel init so MediaSession is active right from the start
        try {
            val initialIntent = Intent(application, TtsPlaybackService::class.java).apply {
                putExtra("BOOK_TITLE", bookConfig.titleEn)
                putExtra("IS_PLAYING", false)
            }
            ContextCompat.startForegroundService(application, initialIntent)
        } catch (e: Exception) {}

        // Listen to playback state to update the foreground service
        viewModelScope.launch {
            isPlaying.collect { playing ->
                val intent = Intent(application, TtsPlaybackService::class.java).apply {
                    putExtra("BOOK_TITLE", bookConfig.titleEn)
                    putExtra("IS_PLAYING", playing)
                }
                try {
                    ContextCompat.startForegroundService(application, intent)
                } catch (e: Exception) {}
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
            
            val willShowPaywall = shouldShowSoftPaywall(number)
            val effectiveAutoPlay = autoPlay && !willShowPaywall
            val effectiveSelectOnLoad = selectOnLoad || (autoPlay && willShowPaywall)

            if ((effectiveAutoPlay || effectiveSelectOnLoad) && sentenceQueue.isNotEmpty()) {
                if (playFromEnd) {
                    var idx = sentenceQueue.size - 1
                    while (idx >= 0) {
                        val s = sentenceQueue[idx]
                        val shouldRead = when (s.lang) {
                            Language.EN -> readEn.value
                            Language.KO -> readKo.value
                        }
                        if (shouldRead) break
                        idx--
                    }
                    currentQueueIndex = if (idx >= 0) idx else sentenceQueue.size - 1
                } else {
                    currentQueueIndex = 0
                }
                playCurrentSequence(play = effectiveAutoPlay)
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
            val sentences = mapOf(
                Language.EN to SentenceSplitter.split(paragraph.en, Language.EN, paragraph.id),
                Language.KO to SentenceSplitter.split(paragraph.ko, Language.KO, paragraph.id)
            )
            
            for (lang in languageOrder.value) {
                sentences[lang]?.let { queue.addAll(it) }
            }
        }
        sentenceQueue = queue
    }

    /** Rebuild queue when Language Order changes */
    fun updateLanguageOrder(order: List<Language>) {
        languageOrder.value = order
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

    fun isChapterAccessible(chapterNumber: Int): Boolean {
        if (billingManager.isFullUnlocked.value) return true
        val maxAccessible = maxOf(bookConfig.freeChapters, _bypassedUpToChapter.value + 2)
        return chapterNumber <= maxAccessible
    }

    fun shouldShowSoftPaywall(chapterNumber: Int): Boolean {
        return !isChapterAccessible(chapterNumber)
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
        if (isPlaying.value) {
            wasPlayingBeforeFocusLoss = false
            _isPlaying.value = false
            ttsManager.stop()
            sendSetPlaying(false)
        } else {
            if (currentQueueIndex == -1 && sentenceQueue.isNotEmpty()) {
                currentQueueIndex = 0
            }
            if (currentQueueIndex in sentenceQueue.indices) {
                playCurrentSequence()
            }
        }
    }

    /** Explicitly update the MediaSession PlaybackState — called only on user play/pause, not per-sentence */
    private fun sendSetPlaying(playing: Boolean) {
        val intent = Intent(getApplication<android.app.Application>(), com.tkprof.shared.tts.TtsPlaybackService::class.java).apply {
            action = "SET_PLAYING"
            putExtra("IS_PLAYING", playing)
        }
        ContextCompat.startForegroundService(getApplication(), intent)
    }

    fun nextSentence() {
        ttsManager.stop()
        
        var tempIndex = currentQueueIndex + 1
        while (tempIndex < sentenceQueue.size) {
            val s = sentenceQueue[tempIndex]
            val shouldRead = when (s.lang) {
                Language.EN -> readEn.value
                Language.KO -> readKo.value
            }
            if (shouldRead) break
            tempIndex++
        }

        if (tempIndex < sentenceQueue.size) {
            currentQueueIndex = tempIndex
            playCurrentSequence(play = true)
        } else {
            val next = _currentChapterNumber.value + 1
            if (next <= _totalChapters.value) {
                loadChapter(next, autoPlay = true, selectOnLoad = false)
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
            val shouldRead = when (s.lang) {
                Language.EN -> readEn.value
                Language.KO -> readKo.value
            }
            if (shouldRead) break
            tempIndex--
        }

        if (tempIndex >= 0) {
            currentQueueIndex = tempIndex
            playCurrentSequence(play = true)
        } else {
            val prev = _currentChapterNumber.value - 1
            if (prev >= 1) {
                loadChapter(prev, autoPlay = true, playFromEnd = true, selectOnLoad = false)
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
                if (next <= _totalChapters.value) {
                    loadChapter(next, autoPlay = play, selectOnLoad = !play)
                    return
                }
            }
            _speakingSentenceId.value = null
            _speakingParagraphIndex.value = -1
            _isPlaying.value = false
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
        
        if (!_isPlaying.value) {
            _isPlaying.value = true
            sendSetPlaying(true)
        }
        
        // Check if we should read this language
        val shouldRead = when (s.lang) {
            Language.EN -> readEn.value
            Language.KO -> readKo.value
        }
        
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

        when (s.lang) {
            Language.KO -> ttsManager.speakKorean(s.text, onDone)
            else -> ttsManager.speakEnglish(s.text, onDone)
        }
    }

    fun stopSpeaking() {
        wasPlayingBeforeFocusLoss = false
        ttsManager.stop()

        _speakingSentenceId.value = null
    }

}


