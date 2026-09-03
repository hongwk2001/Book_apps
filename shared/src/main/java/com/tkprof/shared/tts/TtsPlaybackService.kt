package com.tkprof.shared.tts

import android.app.Notification
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.media.AudioAttributes
import android.media.AudioFormat
import android.media.AudioTrack
import android.os.Build
import android.os.Bundle
import android.os.PowerManager
import androidx.core.app.NotificationCompat
import androidx.core.content.IntentCompat
import androidx.media.MediaBrowserServiceCompat
import androidx.media.session.MediaButtonReceiver

import android.support.v4.media.MediaBrowserCompat
import android.support.v4.media.MediaMetadataCompat
import android.support.v4.media.session.MediaSessionCompat
import android.support.v4.media.session.PlaybackStateCompat

class TtsPlaybackService : MediaBrowserServiceCompat() {

    private var mediaSession: MediaSessionCompat? = null
    private var isMediaPlaying = false
    private var silentAudioTrack: AudioTrack? = null
    private var wakeLock: PowerManager.WakeLock? = null

    private fun startSilentAudio() {
        if (silentAudioTrack != null) {
            try {
                if (silentAudioTrack?.playState != AudioTrack.PLAYSTATE_PLAYING) {
                    silentAudioTrack?.play()
                }
            } catch (_: Exception) {}
            return
        }
        try {
            val sampleRate = 44100
            val bufferSize = AudioTrack.getMinBufferSize(
                sampleRate,
                AudioFormat.CHANNEL_OUT_MONO,
                AudioFormat.ENCODING_PCM_16BIT
            ).coerceAtLeast(sampleRate * 2)

            val silentData = ByteArray(bufferSize)

            val track = AudioTrack.Builder()
                .setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                        .build()
                )
                .setAudioFormat(
                    AudioFormat.Builder()
                        .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
                        .setSampleRate(sampleRate)
                        .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
                        .build()
                )
                .setBufferSizeInBytes(bufferSize)
                .setTransferMode(AudioTrack.MODE_STATIC)
                .build()

            track.write(silentData, 0, silentData.size)
            track.setLoopPoints(0, silentData.size / 2, -1)
            track.play()
            silentAudioTrack = track
        } catch (_: Exception) {}
    }

    private fun pauseSilentAudio() {
        try {
            if (silentAudioTrack?.playState == AudioTrack.PLAYSTATE_PLAYING) {
                silentAudioTrack?.pause()
            }
        } catch (_: Exception) {}
    }

    private fun stopSilentAudio() {
        try {
            silentAudioTrack?.stop()
            silentAudioTrack?.release()
        } catch (_: Exception) {}
        finally {
            silentAudioTrack = null
        }
    }

    // ── MediaBrowserServiceCompat required stubs ──────────────────────────────
    // These make the system (Samsung Now Bar, BT AVRCP, Android Auto) recognise
    // us as a first-class media app rather than a plain foreground service.

    override fun onGetRoot(
        clientPackageName: String,
        clientUid: Int,
        rootHints: Bundle?
    ): BrowserRoot = BrowserRoot("root", null)

    override fun onLoadChildren(
        parentId: String,
        result: Result<List<MediaBrowserCompat.MediaItem>>
    ) {
        result.sendResult(emptyList())
    }
    // ─────────────────────────────────────────────────────────────────────────

    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()

        mediaSession = MediaSessionCompat(this, "TtsPlaybackService").apply {
            setFlags(
                MediaSessionCompat.FLAG_HANDLES_MEDIA_BUTTONS or
                MediaSessionCompat.FLAG_HANDLES_TRANSPORT_CONTROLS
            )
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

                override fun onMediaButtonEvent(mediaButtonEvent: Intent?): Boolean {
                    val keyEvent = mediaButtonEvent?.let {
                        IntentCompat.getParcelableExtra(
                            it,
                            Intent.EXTRA_KEY_EVENT,
                            android.view.KeyEvent::class.java
                        )
                    } ?: mediaButtonEvent?.getParcelableExtra(Intent.EXTRA_KEY_EVENT)
                        as? android.view.KeyEvent

                    if (keyEvent != null) {
                        if (keyEvent.action == android.view.KeyEvent.ACTION_DOWN) {
                            when (keyEvent.keyCode) {
                                android.view.KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE,
                                android.view.KeyEvent.KEYCODE_HEADSETHOOK -> {
                                    if (isMediaPlaying) {
                                        updatePlaybackState(false)
                                        onPause()
                                    } else {
                                        updatePlaybackState(true)
                                        onPlay()
                                    }
                                    return true
                                }
                                android.view.KeyEvent.KEYCODE_MEDIA_PLAY -> {
                                    updatePlaybackState(true)
                                    onPlay()
                                    return true
                                }
                                android.view.KeyEvent.KEYCODE_MEDIA_PAUSE -> {
                                    updatePlaybackState(false)
                                    onPause()
                                    return true
                                }
                                android.view.KeyEvent.KEYCODE_MEDIA_NEXT -> {
                                    onSkipToNext()
                                    return true
                                }
                                android.view.KeyEvent.KEYCODE_MEDIA_PREVIOUS -> {
                                    onSkipToPrevious()
                                    return true
                                }
                            }
                        } else if (keyEvent.action == android.view.KeyEvent.ACTION_UP) {
                            // Consume ACTION_UP so OS does not propagate to Spotify
                            when (keyEvent.keyCode) {
                                android.view.KeyEvent.KEYCODE_MEDIA_PLAY_PAUSE,
                                android.view.KeyEvent.KEYCODE_HEADSETHOOK,
                                android.view.KeyEvent.KEYCODE_MEDIA_PLAY,
                                android.view.KeyEvent.KEYCODE_MEDIA_PAUSE,
                                android.view.KeyEvent.KEYCODE_MEDIA_NEXT,
                                android.view.KeyEvent.KEYCODE_MEDIA_PREVIOUS -> return true
                            }
                        }
                    }
                    return super.onMediaButtonEvent(mediaButtonEvent)
                }
            })

            val pendingIntent = MediaButtonReceiver.buildMediaButtonPendingIntent(
                this@TtsPlaybackService,
                PlaybackStateCompat.ACTION_PLAY_PAUSE
            )
            setMediaButtonReceiver(pendingIntent)
            isActive = true
        }

        // Register session token with MediaBrowserServiceCompat — required so
        // Samsung Now Bar and BT devices discover us as the active media app.
        sessionToken = mediaSession?.sessionToken

        // Initialize state to PAUSED by default on service creation
        updatePlaybackState(false)
    }

    override fun onDestroy() {
        try {
            if (wakeLock?.isHeld == true) {
                wakeLock?.release()
            }
        } catch (_: Exception) {}
        wakeLock = null
        stopSilentAudio()
        mediaSession?.isActive = false
        mediaSession?.release()
        super.onDestroy()
    }

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val bookTitle = intent?.getStringExtra("BOOK_TITLE") ?: "Audiobook"
        val isPlayingForNotification = intent?.getBooleanExtra("IS_PLAYING", isMediaPlaying) ?: isMediaPlaying
        val notification = createNotification(bookTitle, isPlayingForNotification)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            startForeground(1, notification, android.content.pm.ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK)
        } else {
            startForeground(1, notification)
        }

        when (intent?.action) {
            Intent.ACTION_MEDIA_BUTTON -> {
                MediaButtonReceiver.handleIntent(mediaSession, intent)
                return START_STICKY
            }
            "STOP_SERVICE" -> {
                updatePlaybackState(false)
                stopForeground(STOP_FOREGROUND_REMOVE)
                stopSelf()
                return START_NOT_STICKY
            }
            "SET_PLAYING" -> {
                // Only this action changes MediaSession PlaybackState — not per-sentence
                val playing = intent.getBooleanExtra("IS_PLAYING", false)
                updatePlaybackState(playing)
                return START_STICKY
            }
            "PAUSE" -> sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE").apply { setPackage(packageName) })
            "PLAY"  -> sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY").apply { setPackage(packageName) })
            "NEXT"  -> sendBroadcast(Intent("com.tkprof.shared.TTS_NEXT").apply { setPackage(packageName) })
            "PREV"  -> sendBroadcast(Intent("com.tkprof.shared.TTS_PREV").apply { setPackage(packageName) })
        }

        // If an explicit IS_PLAYING extra was supplied without a specific action, ensure playback state matches
        if (intent?.hasExtra("IS_PLAYING") == true) {
            updatePlaybackState(intent.getBooleanExtra("IS_PLAYING", false))
        }

        return START_STICKY
    }

    private fun updatePlaybackState(isPlaying: Boolean) {
        isMediaPlaying = isPlaying
        if (isPlaying) {
            startSilentAudio()
            if (wakeLock == null) {
                val powerManager = getSystemService(Context.POWER_SERVICE) as? PowerManager
                wakeLock = powerManager?.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "BookApps:TtsWakeLock")
            }
            try {
                if (wakeLock?.isHeld != true) {
                    wakeLock?.acquire(60 * 60 * 1000L) // 60 min safety timeout
                }
            } catch (_: Exception) {}
        } else {
            pauseSilentAudio()
            try {
                if (wakeLock?.isHeld == true) {
                    wakeLock?.release()
                }
            } catch (_: Exception) {}
        }
        val state = if (isPlaying) PlaybackStateCompat.STATE_PLAYING else PlaybackStateCompat.STATE_PAUSED
        mediaSession?.setPlaybackState(
            PlaybackStateCompat.Builder()
                .setActions(
                    PlaybackStateCompat.ACTION_PLAY or
                    PlaybackStateCompat.ACTION_PAUSE or
                    PlaybackStateCompat.ACTION_PLAY_PAUSE or
                    PlaybackStateCompat.ACTION_SKIP_TO_NEXT or
                    PlaybackStateCompat.ACTION_SKIP_TO_PREVIOUS or
                    PlaybackStateCompat.ACTION_STOP
                )
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
