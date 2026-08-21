import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'r', encoding='utf-8') as f:
    text = f.read()

old_builder = '''        val builder = NotificationCompat.Builder(this, "tts_channel")
            .setContentTitle(title)
            .setContentText("Audiobook Playback")
            .setSmallIcon(android.R.drawable.ic_media_play)
            .setOngoing(isPlaying)
            .setStyle(androidx.media.app.NotificationCompat.MediaStyle().setMediaSession(mediaSession?.sessionToken))
            .setDeleteIntent(stopPendingIntent)
            
        if (isPlaying) {
            builder.addAction(android.R.drawable.ic_media_pause, "Pause", pausePendingIntent)
        } else {
            builder.addAction(android.R.drawable.ic_media_play, "Play", playPendingIntent)
        }'''

new_builder = '''        val builder = NotificationCompat.Builder(this, "tts_channel")
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

text = text.replace(old_builder, new_builder)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'w', encoding='utf-8') as f:
    f.write(text)
