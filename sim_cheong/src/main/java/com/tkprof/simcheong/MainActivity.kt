package com.tkprof.simcheong

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
 * 홍길동전 (The Story of Hong Gildong) app entry point.
 * All reader logic lives in :shared — this file only defines the book config.
 *
 * Text: the 36장 완판본 「홍길동전」 (공유마당, 자유이용 만료); built from hong_gildong/content.
 */
class MainActivity : ComponentActivity() {

    private lateinit var ttsManager: TtsManager
    private lateinit var billingManager: BillingManager
    private lateinit var viewModel: ReaderViewModel

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        volumeControlStream = android.media.AudioManager.STREAM_MUSIC

        val bookConfig = BookConfig(
            bookId = "sim_cheong",
            titleEn = "The Story of Shim Cheong",
            titleKo = "심청전",
            author = "Anonymous (Wanpan edition, public domain)",
            totalChapters = 13,
            freeChapters = 3,
            iapProductId = "com.tkprof.simcheong.full"
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
