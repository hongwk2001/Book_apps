import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = '''        // Listen to TTS state to update the foreground service
        viewModelScope.launch {
            isSpeaking.collect { speaking ->
                val intent = Intent(application, TtsPlaybackService::class.java).apply {
                    putExtra("BOOK_TITLE", bookConfig.titleEn)
                    putExtra("IS_PLAYING", speaking)
                }
                ContextCompat.startForegroundService(application, intent)
            }
        }'''

new_code = '''        // Listen to TTS state to update the foreground service
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
        }'''

text = text.replace(old_code, new_code)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(text)
