package com.tkprof.shared.tts

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.app.Service
import android.content.Intent
import android.os.Build
import android.os.IBinder
import androidx.core.app.NotificationCompat
import com.tkprof.shared.R

import android.support.v4.media.session.MediaSessionCompat
import android.support.v4.media.MediaMetadataCompat
import android.support.v4.media.session.PlaybackStateCompat

class TtsPlaybackService : Service() {

    private var mediaSession: MediaSessionCompat? = null

    override fun onBind(intent: Intent?): IBinder? = null

    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()
        
        mediaSession = MediaSessionCompat(this, "TtsPlaybackService").apply {
            setCallback(object : MediaSessionCompat.Callback() {
                override fun onPlay() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY").apply { setPackage(packageName) })
                }
                override fun onPause() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE").apply { setPackage(packageName) })
                }
                override fun onSkipToNext() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_NEXT").apply { setPackage(packageName) })
                }
                override fun onSkipToPrevious() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PREV").apply { setPackage(packageName) })
                }
            })
            isActive = true
        }
    }
    
    override fun onDestroy() {
        mediaSession?.release()
        super.onDestroy()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val bookTitle = intent?.getStringExtra("BOOK_TITLE") ?: "Audiobook"
        val isPlaying = intent?.getBooleanExtra("IS_PLAYING", true) ?: true
        val notification = createNotification(bookTitle, isPlaying)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            startForeground(1, notification, android.content.pm.ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK)
        } else {
            startForeground(1, notification)
        }

        val action = intent?.action
        if (action == "STOP_SERVICE") {
            stopForeground(STOP_FOREGROUND_REMOVE)
            stopSelf()
            return START_NOT_STICKY
        }
        
        if (action == "PAUSE") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE").apply { setPackage(packageName) })
        } else if (action == "PLAY") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY").apply { setPackage(packageName) })
        } else if (action == "NEXT") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_NEXT").apply { setPackage(packageName) })
        } else if (action == "PREV") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PREV").apply { setPackage(packageName) })
        }

        updatePlaybackState(isPlaying)

        return START_STICKY
    }
    
    private fun updatePlaybackState(isPlaying: Boolean) {
        val state = if (isPlaying) PlaybackStateCompat.STATE_PLAYING else PlaybackStateCompat.STATE_PAUSED
        mediaSession?.setPlaybackState(
            PlaybackStateCompat.Builder()
                .setActions(PlaybackStateCompat.ACTION_PLAY or PlaybackStateCompat.ACTION_PAUSE or PlaybackStateCompat.ACTION_SKIP_TO_NEXT or PlaybackStateCompat.ACTION_SKIP_TO_PREVIOUS or PlaybackStateCompat.ACTION_STOP)
                .setState(state, PlaybackStateCompat.PLAYBACK_POSITION_UNKNOWN, 1.0f)
                .build()
        )
    }

    private fun createNotification(title: String, isPlaying: Boolean): Notification {
        mediaSession?.setMetadata(
            MediaMetadataCompat.Builder()
                .putString(MediaMetadataCompat.METADATA_KEY_TITLE, title)
                .putString(MediaMetadataCompat.METADATA_KEY_ARTIST, "TKProf Book")
                .build()
        )

        val stopIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "STOP_SERVICE" }
        val stopPendingIntent = PendingIntent.getService(this, 0, stopIntent, PendingIntent.FLAG_IMMUTABLE)
        
        val playIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "PLAY" }
        val playPendingIntent = PendingIntent.getService(this, 1, playIntent, PendingIntent.FLAG_IMMUTABLE)
        
        val pauseIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "PAUSE" }
                val pausePendingIntent = PendingIntent.getService(this, 2, pauseIntent, PendingIntent.FLAG_IMMUTABLE)

        val prevIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "PREV" }
        val prevPendingIntent = PendingIntent.getService(this, 3, prevIntent, PendingIntent.FLAG_IMMUTABLE)
        
        val nextIntent = Intent(this, TtsPlaybackService::class.java).apply { action = "NEXT" }
        val nextPendingIntent = PendingIntent.getService(this, 4, nextIntent, PendingIntent.FLAG_IMMUTABLE)

        val builder = NotificationCompat.Builder(this, "tts_channel")
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
        )
            
        return builder.build()
    }

    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                "tts_channel",
                "Audiobook Playback",
                NotificationManager.IMPORTANCE_LOW
            ).apply {
                description = "Keeps the audiobook playing while the screen is off."
            }
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(channel)
        }
    }
}
