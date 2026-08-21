import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Add missing androidx.media imports if they are not there
if 'androidx.media' not in text:
    pass # we added android.support.v4.media

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'w', encoding='utf-8') as f:
    f.write(text)
