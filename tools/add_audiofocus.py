import sys

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    content = f.read()

# Add imports
imports = '''import android.media.AudioManager
import android.media.AudioFocusRequest
import android.content.Context
import android.os.Build
'''
content = content.replace('import androidx.lifecycle.ViewModel', imports + 'import androidx.lifecycle.ViewModel')

# Add AudioFocus fields
fields = '''
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
'''
content = content.replace('private val _speakingParagraphIndex = MutableStateFlow(-1)', fields + '\n    private val _speakingParagraphIndex = MutableStateFlow(-1)')

# Inject into playCurrentSequence
play_start = '''    private fun playCurrentSequence() {
        if (!requestAudioFocus()) return
'''
content = content.replace('    private fun playCurrentSequence() {', play_start)

# Inject abandon into stop
stop_logic = '''    fun stopSpeaking() {
        wasPlayingBeforeFocusLoss = false
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) {
            @Suppress("DEPRECATION")
            audioManager.abandonAudioFocus(audioFocusChangeListener)
        }
        ttsManager.stop()
'''
content = content.replace('    fun stopSpeaking() {\n        ttsManager.stop()', stop_logic)

# Wait, playOrPause also does ttsManager.stop()
play_pause_logic = '''    fun playOrPause() {
        if (isSpeaking.value) {
            wasPlayingBeforeFocusLoss = false
            ttsManager.stop()
'''
content = content.replace('''    fun playOrPause() {
        if (isSpeaking.value) {
            ttsManager.stop()''', play_pause_logic)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(content)
