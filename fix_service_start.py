import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace the foreground service logic in init { }
old_code = '''        // Listen to TTS state to start/stop the foreground service
        viewModelScope.launch {
            isSpeaking.collect { speaking ->
                val intent = Intent(application, TtsPlaybackService::class.java)
                if (speaking) {
                    intent.putExtra("BOOK_TITLE", bookConfig.titleEn)
                    ContextCompat.startForegroundService(application, intent)
                } else {
                    application.stopService(intent)
                }
            }
        }'''

new_code = '''        // Listen to TTS state to update the foreground service
        viewModelScope.launch {
            isSpeaking.collect { speaking ->
                val intent = Intent(application, TtsPlaybackService::class.java).apply {
                    putExtra("BOOK_TITLE", bookConfig.titleEn)
                    putExtra("IS_PLAYING", speaking)
                }
                ContextCompat.startForegroundService(application, intent)
            }
        }'''

text = text.replace(old_code, new_code)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(text)
