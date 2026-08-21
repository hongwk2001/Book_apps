package com.tkprof.secretgarden

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import com.tkprof.shared.billing.BillingManager
import com.tkprof.shared.model.BookConfig
import com.tkprof.shared.theme.TKProfReaderTheme
import com.tkprof.shared.tts.TtsManager
import com.tkprof.shared.ui.reader.ReaderScreen
import com.tkprof.shared.ui.reader.ReaderViewModel

/**
 * Dracula app entry point.
 * All reader logic lives in :shared — this file only defines the book config.
 */
class MainActivity : ComponentActivity() {

    private lateinit var ttsManager: TtsManager
    private lateinit var billingManager: BillingManager
    private lateinit var viewModel: ReaderViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        volumeControlStream = android.media.AudioManager.STREAM_MUSIC

        val bookConfig = BookConfig(
            bookId = "secretgarden",
            titleEn = "Secret Garden",
            titleKo = "비밀의 화원",
            author = "Frances Hodgson Burnett",
            totalChapters = 27,
            freeChapters = 2,
            iapProductId = "com.tkprof.secretgarden.full"
        )

        ttsManager = TtsManager(applicationContext).also { it.init() }
        billingManager = BillingManager(applicationContext, bookConfig.iapProductId).also { it.init() }

        viewModel = ViewModelProvider(this, object : ViewModelProvider.Factory {
            @Suppress("UNCHECKED_CAST")
            override fun <T : ViewModel> create(modelClass: Class<T>): T =
                ReaderViewModel(application, bookConfig, ttsManager, billingManager) as T
        })[ReaderViewModel::class.java]

        enableEdgeToEdge()
        setContent {
            TKProfReaderTheme {
                ReaderScreen(viewModel = viewModel)
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        if (!isChangingConfigurations) {
            ttsManager.shutdown()
            billingManager.disconnect()
        }
    }
}
