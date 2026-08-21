import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'r', encoding='utf-8') as f:
    text = f.read()

old_rx = '''            when (intent?.action) {
                "com.tkprof.shared.TTS_PLAY" -> {
                    if (!ttsManager.isSpeaking.value) playOrPause()
                }
                "com.tkprof.shared.TTS_PAUSE" -> {
                    if (ttsManager.isSpeaking.value) playOrPause()
                }
            }'''
            
new_rx = '''            when (intent?.action) {
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
            }'''

text = text.replace(old_rx, new_rx)

old_filter = '''            android.content.IntentFilter().apply {
                addAction("com.tkprof.shared.TTS_PLAY")
                addAction("com.tkprof.shared.TTS_PAUSE")
            }'''
            
new_filter = '''            android.content.IntentFilter().apply {
                addAction("com.tkprof.shared.TTS_PLAY")
                addAction("com.tkprof.shared.TTS_PAUSE")
                addAction("com.tkprof.shared.TTS_NEXT")
                addAction("com.tkprof.shared.TTS_PREV")
            }'''
            
text = text.replace(old_filter, new_filter)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderViewModel.kt', 'w', encoding='utf-8') as f:
    f.write(text)
