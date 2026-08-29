package com.tkprof.shared.ui.reader

import android.app.Application
import android.content.Context
import android.content.SharedPreferences
import android.media.AudioManager
import com.tkprof.shared.billing.BillingManager
import com.tkprof.shared.model.BookConfig
import com.tkprof.shared.tts.TtsManager
import io.mockk.every
import io.mockk.just
import io.mockk.Runs
import io.mockk.mockk
import io.mockk.mockkStatic
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class ReaderViewModelTest {

    private lateinit var viewModel: ReaderViewModel
    private val testDispatcher = StandardTestDispatcher()

    private val application = mockk<Application>(relaxed = true)
    private val sharedPrefs = mockk<SharedPreferences>(relaxed = true)
    private val sharedPrefsEditor = mockk<SharedPreferences.Editor>(relaxed = true)
    private val ttsManager = mockk<TtsManager>(relaxed = true)
    private val billingManager = mockk<BillingManager>(relaxed = true)
    private val audioManager = mockk<AudioManager>(relaxed = true)

    private val isFullUnlockedFlow = MutableStateFlow(false)

    @Before
    fun setup() {
        Dispatchers.setMain(testDispatcher)

        mockkStatic(androidx.core.content.ContextCompat::class)
        every { androidx.core.content.ContextCompat.registerReceiver(any(), any(), any(), any()) } returns mockk(relaxed = true)
        every { androidx.core.content.ContextCompat.startForegroundService(any(), any()) } just Runs

        every { application.getSharedPreferences("ReaderPrefs", Context.MODE_PRIVATE) } returns sharedPrefs
        every { application.getSystemService(Context.AUDIO_SERVICE) } returns audioManager
        
        every { sharedPrefs.getInt("bypassed_up_to_chapter", 0) } returns 0
        every { sharedPrefs.edit() } returns sharedPrefsEditor
        every { sharedPrefsEditor.putInt(any(), any()) } returns sharedPrefsEditor

        every { billingManager.isFullUnlocked } returns isFullUnlockedFlow
        every { ttsManager.isSpeaking } returns MutableStateFlow(false)

        val bookConfig = BookConfig(
            bookId = "test_book",
            titleEn = "Test",
            titleKo = "테스트",
            author = "Author",
            totalChapters = 10,
            freeChapters = 2,
            iapProductId = "com.test.full"
        )

        viewModel = ReaderViewModel(application, bookConfig, ttsManager, billingManager)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun shouldShowSoftPaywall_isFalse_whenFullUnlocked() {
        isFullUnlockedFlow.value = true

        assertFalse(viewModel.shouldShowSoftPaywall(3))
        assertFalse(viewModel.shouldShowSoftPaywall(6))
    }

    @Test
    fun shouldShowSoftPaywall_isTrue_forLockedChapters() {
        isFullUnlockedFlow.value = false

        assertFalse("Chapter 1 is free, should not show paywall", viewModel.shouldShowSoftPaywall(1))
        assertFalse("Chapter 2 is free, should not show paywall", viewModel.shouldShowSoftPaywall(2))
        assertTrue("Chapter 3 is locked, should show paywall", viewModel.shouldShowSoftPaywall(3))
        assertTrue("Chapter 4 is locked, should show paywall", viewModel.shouldShowSoftPaywall(4))
        assertTrue("Chapter 6 is locked, should show paywall", viewModel.shouldShowSoftPaywall(6))
    }

    @Test
    fun shouldShowSoftPaywall_isFalse_ifBypassed() {
        isFullUnlockedFlow.value = false

        assertTrue("Initially Chapter 3 shows paywall", viewModel.shouldShowSoftPaywall(3))

        // Simulate navigating to chapter 3 and bypassing it
        viewModel.loadChapter(3, autoPlay = false, selectOnLoad = false)
        while (viewModel.currentChapterNumber.value != 3) {
            Thread.sleep(10)
        }
        viewModel.bypassSoftPaywall()

        assertFalse("Chapter 3 is now bypassed", viewModel.shouldShowSoftPaywall(3))
        assertFalse("Chapter 4 is now bypassed", viewModel.shouldShowSoftPaywall(4))
        assertFalse("Chapter 5 is now bypassed", viewModel.shouldShowSoftPaywall(5))
        assertTrue("Chapter 6 is now locked again", viewModel.shouldShowSoftPaywall(6))
        
        // Bypass chapter 6
        viewModel.loadChapter(6, autoPlay = false, selectOnLoad = false)
        while (viewModel.currentChapterNumber.value != 6) {
            Thread.sleep(10)
        }
        viewModel.bypassSoftPaywall()
        assertFalse("Chapter 6 is now bypassed", viewModel.shouldShowSoftPaywall(6))
    }
}
