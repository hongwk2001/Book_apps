import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Add Next/Prev intents
intents = '''        val pausePendingIntent = PendingIntent.getService(this, 2, pauseIntent, PendingIntent.FLAG_IMMUTABLE)

        val prevIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "PREV" }
        val prevPendingIntent = PendingIntent.getService(this, 3, prevIntent, PendingIntent.FLAG_IMMUTABLE)
        
        val nextIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "NEXT" }
        val nextPendingIntent = PendingIntent.getService(this, 4, nextIntent, PendingIntent.FLAG_IMMUTABLE)'''

text = text.replace('val pausePendingIntent = PendingIntent.getService(this, 2, pauseIntent, PendingIntent.FLAG_IMMUTABLE)', intents)

# Update builder
old_builder = '''        val builder = NotificationCompat.Builder(this, "tts_channel")
            .setContentTitle(title)
            .setContentText("Audiobook Playback")
            .setSmallIcon(android.R.drawable.ic_media_play)
            .setOngoing(isPlaying)
            .setDeleteIntent(stopPendingIntent)
            
        if (isPlaying) {
            builder.addAction(android.R.drawable.ic_media_pause, "Pause", pausePendingIntent)
        } else {
            builder.addAction(android.R.drawable.ic_media_play, "Play", playPendingIntent)
        }
        
        builder.addAction(android.R.drawable.ic_menu_close_clear_cancel, "Stop", stopPendingIntent)
        
        // Show the actions in the compact view
        builder.setStyle(
            androidx.media.app.NotificationCompat.MediaStyle()
                .setMediaSession(mediaSession?.sessionToken)
                .setShowActionsInCompactView(0, 1) // 0 is Play/Pause, 1 is Stop
        )'''

new_builder = '''        val builder = NotificationCompat.Builder(this, "tts_channel")
            .setContentTitle(title)
            .setContentText("Audiobook Playback")
            .setSmallIcon(android.R.drawable.ic_media_play)
            .setOngoing(isPlaying)
            .setDeleteIntent(stopPendingIntent)
            
        builder.addAction(android.R.drawable.ic_media_previous, "Previous", prevPendingIntent)
            
        if (isPlaying) {
            builder.addAction(android.R.drawable.ic_media_pause, "Pause", pausePendingIntent)
        } else {
            builder.addAction(android.R.drawable.ic_media_play, "Play", playPendingIntent)
        }
        
        builder.addAction(android.R.drawable.ic_media_next, "Next", nextPendingIntent)
        builder.addAction(android.R.drawable.ic_menu_close_clear_cancel, "Stop", stopPendingIntent)
        
        // Show Prev, Play/Pause, Next in compact view (indices 0, 1, 2)
        builder.setStyle(
            androidx.media.app.NotificationCompat.MediaStyle()
                .setMediaSession(mediaSession?.sessionToken)
                .setShowActionsInCompactView(0, 1, 2)
        )'''
        
text = text.replace(old_builder, new_builder)

# Update onStartCommand to handle NEXT/PREV
old_start = '''        if (action == "PAUSE") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
        } else if (action == "PLAY") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
        }'''
        
new_start = '''        if (action == "PAUSE") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
        } else if (action == "PLAY") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
        } else if (action == "NEXT") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_NEXT"))
        } else if (action == "PREV") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PREV"))
        }'''
        
text = text.replace(old_start, new_start)

# Update MediaSession callbacks
old_cb = '''            setCallback(object : MediaSessionCompat.Callback() {
                override fun onPlay() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
                }
                override fun onPause() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
                }
            })'''

new_cb = '''            setCallback(object : MediaSessionCompat.Callback() {
                override fun onPlay() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
                }
                override fun onPause() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
                }
                override fun onSkipToNext() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_NEXT"))
                }
                override fun onSkipToPrevious() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PREV"))
                }
            })'''
            
text = text.replace(old_cb, new_cb)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'w', encoding='utf-8') as f:
    f.write(text)
