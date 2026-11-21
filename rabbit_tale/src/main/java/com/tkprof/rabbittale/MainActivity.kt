package com.tkprof.rabbittale

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
 * 토끼전 (The Rabbit Tale) app entry point.
 * All reader logic lives in :shared — this file only defines the book config.
 *
 * Text: 주부전 (토끼전), Wikisource transcription of the 국립한글박물관 manuscript, PD-anon-US;
 * drafted from TKprof_book/books/rabbit_tale.
 */
class MainActivity : ComponentActivity() {

    private lateinit var ttsManager: TtsManager
    private lateinit var billingManager: BillingManager
    private lateinit var viewModel: ReaderViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        volumeControlStream = android.media.AudioManager.STREAM_MUSIC

        val bookConfig = BookConfig(
            bookId = "rabbit_tale",
            titleEn = "The Rabbit Tale",
            titleKo = "토끼전",
            author = "Anonymous (주부전 edition, public domain)",
            totalChapters = 12,
            freeChapters = 3,
            iapProductId = "com.tkprof.rabbittale.full"
        )

        ttsManager = TtsManager(applicationContext).also { it.init() }
        val tipProductIds = listOf("tip_small_1500", "tip_medium_3000", "tip_large_5000")
        billingManager = BillingManager(applicationContext, tipProductIds).also { it.init() }

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
