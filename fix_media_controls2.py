import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update PlaybackState actions
old_state = '''            PlaybackStateCompat.Builder()
                .setActions(PlaybackStateCompat.ACTION_PLAY or PlaybackStateCompat.ACTION_PAUSE)
                .setState(state, PlaybackStateCompat.PLAYBACK_POSITION_UNKNOWN, 1.0f)
                .build()'''
                
new_state = '''            PlaybackStateCompat.Builder()
                .setActions(PlaybackStateCompat.ACTION_PLAY or PlaybackStateCompat.ACTION_PAUSE or PlaybackStateCompat.ACTION_SKIP_TO_NEXT or PlaybackStateCompat.ACTION_SKIP_TO_PREVIOUS or PlaybackStateCompat.ACTION_STOP)
                .setState(state, PlaybackStateCompat.PLAYBACK_POSITION_UNKNOWN, 1.0f)
                .build()'''
                
text = text.replace(old_state, new_state)

# 2. Fix all sendBroadcast calls to set package
text = re.sub(r'sendBroadcast\(Intent\("([^"]+)"\)\)', r'sendBroadcast(Intent("\1").apply { setPackage(packageName) })', text)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'w', encoding='utf-8') as f:
    f.write(text)
