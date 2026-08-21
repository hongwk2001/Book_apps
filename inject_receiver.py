import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    text = f.read()

injection = '''
    private val ttsReceiver = object : android.content.BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            when (intent?.action) {
                "com.tkprof.shared.TTS_PLAY" -> {
                    if (!ttsManager.isSpeaking.value) playOrPause()
                }
                "com.tkprof.shared.TTS_PAUSE" -> {
                    if (ttsManager.isSpeaking.value) playOrPause()
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
            },
            androidx.core.content.ContextCompat.RECEIVER_NOT_EXPORTED
        )
    }
    
    override fun onCleared() {
        super.onCleared()
        try {
            getApplication<Application>().unregisterReceiver(ttsReceiver)
        } catch (e: Exception) {}
    }
'''

if 'ttsReceiver' not in text:
    text = re.sub(r'val fontSizeMultiplier = MutableStateFlow\(1\.0f\)', r'val fontSizeMultiplier = MutableStateFlow(1.0f)\n' + injection, text)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(text)
