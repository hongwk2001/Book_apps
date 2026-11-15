package com.tkprof.midsummer

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
 * 한여름 밤의 꿈 (A Midsummer Night's Dream) app entry point.
 * All reader logic lives in :shared — this file only defines the book config.
 *
 * Text: William Shakespeare, A Midsummer Night's Dream (Project Gutenberg #1514, public domain);
 * built from TKprof_book/books/midsummer.
 */
class MainActivity : ComponentActivity() {

    private lateinit var ttsManager: TtsManager
    private lateinit var billingManager: BillingManager
    private lateinit var viewModel: ReaderViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        volumeControlStream = android.media.AudioManager.STREAM_MUSIC

        val bookConfig = BookConfig(
            bookId = "midsummer",
            titleEn = "A Midsummer Night's Dream",
            titleKo = "한여름 밤의 꿈",
            author = "William Shakespeare (public domain)",
            totalChapters = 9,
            freeChapters = 3,
            iapProductId = "com.tkprof.midsummer.full"
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
