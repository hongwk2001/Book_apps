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

    fun init() {
        tts = TextToSpeech(context) { status ->
            if (status == TextToSpeech.SUCCESS) {
                tts?.setAudioAttributes(
                    android.media.AudioAttributes.Builder()
                        .setUsage(android.media.AudioAttributes.USAGE_MEDIA)
                        .setContentType(android.media.AudioAttributes.CONTENT_TYPE_SPEECH)
                        .build()
                )
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

    fun speakEnglish(text: String, onDone: () -> Unit = {}) {
        val engine = tts ?: return
        engine.setSpeechRate(englishSpeed)
        engine.setPitch(englishPitch)
        selectedEnglishVoice?.let { engine.voice = it } ?: engine.setLanguage(Locale.US)
        
        _isSpeaking.value = true
        engine.speak(text, TextToSpeech.QUEUE_FLUSH, null, "utt_en")
        engine.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(id: String?) {}
            override fun onDone(id: String?) { _isSpeaking.value = false; onDone() }
            @Deprecated("Deprecated in Java")
            override fun onError(id: String?) { _isSpeaking.value = false }
        })
    }

    fun speakKorean(text: String, onDone: () -> Unit = {}) {
        val engine = tts ?: return
        engine.setSpeechRate(koreanSpeed)
        engine.setPitch(koreanPitch)
        selectedKoreanVoice?.let { engine.voice = it } ?: engine.setLanguage(Locale.KOREA)
        
        _isSpeaking.value = true
        engine.speak(text, TextToSpeech.QUEUE_FLUSH, null, "utt_ko")
        engine.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(id: String?) {}
            override fun onDone(id: String?) { _isSpeaking.value = false; onDone() }
            @Deprecated("Deprecated in Java")
            override fun onError(id: String?) { _isSpeaking.value = false }
        })
    }

    fun speakSample(lang: Language, bookTitle: String) {
        when (lang) {
            Language.EN -> speakEnglish("You are listening to $bookTitle. This voice is for English.")
            Language.KO -> speakKorean("${bookTitle}를 듣고 있습니다. 이 음성은 한국어입니다.")
        }
    }

    fun stop() {
        tts?.stop()
        _isSpeaking.value = false
    }

    fun shutdown() {
        tts?.shutdown()
        tts = null
        _isReady.value = false
    }
}
