import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'r', encoding='utf-8') as f:
    text = f.read()

replacement = '''import android.support.v4.media.session.MediaSessionCompat
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
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
                }
                override fun onPause() {
                    sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
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
        val action = intent?.action
        if (action == "STOP_SERVICE") {
            stopForeground(STOP_FOREGROUND_REMOVE)
            stopSelf()
            return START_NOT_STICKY
        }
        
        if (action == "PAUSE") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PAUSE"))
        } else if (action == "PLAY") {
            sendBroadcast(Intent("com.tkprof.shared.TTS_PLAY"))
        }

        val bookTitle = intent?.getStringExtra("BOOK_TITLE") ?: "Audiobook"
        val isPlaying = intent?.getBooleanExtra("IS_PLAYING", true) ?: true
        val notification = createNotification(bookTitle, isPlaying)

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
            startForeground(1, notification, android.content.pm.ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK)
        } else {
            startForeground(1, notification)
        }
        
        updatePlaybackState(isPlaying)

        return START_STICKY
    }
    
    private fun updatePlaybackState(isPlaying: Boolean) {
        val state = if (isPlaying) PlaybackStateCompat.STATE_PLAYING else PlaybackStateCompat.STATE_PAUSED
        mediaSession?.setPlaybackState(
            PlaybackStateCompat.Builder()
                .setActions(PlaybackStateCompat.ACTION_PLAY or PlaybackStateCompat.ACTION_PAUSE)
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

        val builder = NotificationCompat.Builder(this, "tts_channel")
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
        }
            
        return builder.build()
    }'''

# Replace class body
text = re.sub(r'class TtsPlaybackService : Service\(\) \{.*', replacement + '\n\n    private fun createNotificationChannel() {\n        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {\n            val channel = NotificationChannel(\n                "tts_channel",\n                "Audiobook Playback",\n                NotificationManager.IMPORTANCE_LOW\n            ).apply {\n                description = "Keeps the audiobook playing while the screen is off."\n            }\n            val manager = getSystemService(NotificationManager::class.java)\n            manager.createNotificationChannel(channel)\n        }\n    }\n}\n', text, flags=re.DOTALL)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\tts\TtsPlaybackService.kt', 'w', encoding='utf-8') as f:
    f.write(text)
