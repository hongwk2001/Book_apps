package com.tkprof.shared.tts

import android.content.Context
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import android.speech.tts.Voice
import com.tkprof.shared.model.Language
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import java.util.Locale

/**
 * Wraps Android TextToSpeech.
 * Supports Pitch, fine Speed control, and dynamic sample reading.
 */
class TtsManager(private val context: Context) {

    private var tts: TextToSpeech? = null

    private val _isReady = MutableStateFlow(false)
    val isReady: StateFlow<Boolean> = _isReady

    private val _isSpeaking = MutableStateFlow(false)
    val isSpeaking: StateFlow<Boolean> = _isSpeaking

    val englishVoices = MutableStateFlow<List<Voice>>(emptyList())
    val koreanVoices  = MutableStateFlow<List<Voice>>(emptyList())

        var selectedEnglishVoice: Voice? = null
    var selectedKoreanVoice: Voice? = null
    
        var englishSpeed: Float = 1.0f
    var koreanSpeed: Float = 0.9f
    
        var englishPitch: Float = 1.0f
    var koreanPitch: Float = 1.0f

    private var onCurrentUtteranceDone: (() -> Unit)? = null
    private var onCurrentUtteranceError: (() -> Unit)? = null

    fun init() {
        tts = TextToSpeech(context) { status ->
            if (status == TextToSpeech.SUCCESS) {
                tts?.setAudioAttributes(
                    android.media.AudioAttributes.Builder()
                        .setUsage(android.media.AudioAttributes.USAGE_MEDIA)
                        .setContentType(android.media.AudioAttributes.CONTENT_TYPE_SPEECH)
                        .build()
                )
                tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                    override fun onStart(id: String?) {
                        _isSpeaking.value = true
                    }
                    override fun onDone(id: String?) {
                        _isSpeaking.value = false
                        val callback = onCurrentUtteranceDone
                        onCurrentUtteranceDone = null
                        onCurrentUtteranceError = null
                        callback?.invoke()
                    }
                    @Deprecated("Deprecated in Java")
                    override fun onError(id: String?) {
                        _isSpeaking.value = false
                        val callback = onCurrentUtteranceError
                        onCurrentUtteranceDone = null
                        onCurrentUtteranceError = null
                        callback?.invoke()
                    }
                })
                _isReady.value = true
                loadVoices()
            }
        }
    }

    private fun loadVoices() {
        val all = tts?.voices ?: return
        
        // Include all English voices (US, UK, AU, etc.) so they sound different, including network voices
        val enList = all.filter { it.locale.language == "en" }
        englishVoices.value = enList.sortedBy { it.name }
        
        koreanVoices.value = all
            .filter { it.locale.language == "ko" }
            .sortedBy { it.name }
            
        selectedEnglishVoice = englishVoices.value.firstOrNull()
        selectedKoreanVoice  = koreanVoices.value.firstOrNull()
    }

    fun speakEnglish(text: String, onDone: () -> Unit = {}, onError: () -> Unit = {}) {
        val engine = tts ?: run {
            onError()
            return
        }
        engine.setSpeechRate(englishSpeed)
        engine.setPitch(englishPitch)
        selectedEnglishVoice?.let { engine.voice = it } ?: engine.setLanguage(Locale.US)
        
        onCurrentUtteranceDone = onDone
        onCurrentUtteranceError = onError
        _isSpeaking.value = true
        val result = engine.speak(text, TextToSpeech.QUEUE_FLUSH, null, "utt_en_${System.currentTimeMillis()}")
        if (result != TextToSpeech.SUCCESS) {
            _isSpeaking.value = false
            onCurrentUtteranceDone = null
            onCurrentUtteranceError = null
            onError()
        }
    }

    fun speakKorean(text: String, onDone: () -> Unit = {}, onError: () -> Unit = {}) {
        val engine = tts ?: run {
            onError()
            return
        }
        engine.setSpeechRate(koreanSpeed)
        engine.setPitch(koreanPitch)
        selectedKoreanVoice?.let { engine.voice = it } ?: engine.setLanguage(Locale.KOREA)
        
        onCurrentUtteranceDone = onDone
        onCurrentUtteranceError = onError
        _isSpeaking.value = true
        val result = engine.speak(text, TextToSpeech.QUEUE_FLUSH, null, "utt_ko_${System.currentTimeMillis()}")
        if (result != TextToSpeech.SUCCESS) {
            _isSpeaking.value = false
            onCurrentUtteranceDone = null
            onCurrentUtteranceError = null
            onError()
        }
    }

    fun speakSample(lang: Language, bookTitle: String) {
        when (lang) {
            Language.EN -> speakEnglish("You are listening to $bookTitle. This voice is for English.")
            Language.KO -> speakKorean("${bookTitle}를 듣고 있습니다. 이 음성은 한국어입니다.")
        }
    }

    fun stop() {
        onCurrentUtteranceDone = null
        onCurrentUtteranceError = null
        tts?.stop()
        _isSpeaking.value = false
    }

    fun shutdown() {
        onCurrentUtteranceDone = null
        onCurrentUtteranceError = null
        tts?.stop()
        tts?.shutdown()
        tts = null
        _isReady.value = false
        _isSpeaking.value = false
    }
}
