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
import io.mockk.verify
import com.tkprof.shared.model.Language
import org.junit.After
import org.junit.Assert.assertEquals
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
        every { audioManager.requestAudioFocus(any<android.media.AudioFocusRequest>()) } returns AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        every { audioManager.abandonAudioFocusRequest(any<android.media.AudioFocusRequest>()) } returns AudioManager.AUDIOFOCUS_REQUEST_GRANTED
        
        every { sharedPrefs.getInt("bypassed_up_to_chapter", 0) } returns 0
        every { sharedPrefs.edit() } returns sharedPrefsEditor
        every { sharedPrefsEditor.putInt(any(), any()) } returns sharedPrefsEditor
        every { sharedPrefsEditor.putFloat(any(), any()) } returns sharedPrefsEditor
        every { sharedPrefsEditor.putBoolean(any(), any()) } returns sharedPrefsEditor
        every { sharedPrefsEditor.putString(any(), any()) } returns sharedPrefsEditor

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
        awaitChapterLoad()
    }

    /**
     * Wait for the in-flight chapter load to finish. It runs on Dispatchers.IO and
     * rebuilds the sentence queue, so a test that seeds a queue before it completes
     * has that queue pulled out from under it.
     */
    private fun awaitChapterLoad() {
        val jobField = ReaderViewModel::class.java.getDeclaredField("loadJob")
        jobField.isAccessible = true
        val deadline = System.currentTimeMillis() + 5_000
        while (System.currentTimeMillis() < deadline) {
            val job = jobField.get(viewModel) as? kotlinx.coroutines.Job
            if (job != null && job.isCompleted) return
            Thread.sleep(5)
        }
        throw AssertionError("chapter load did not finish in time")
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

    @Test
    fun saveReaderSettings_persistsValuesToSharedPreferences() {
        viewModel.saveReaderSettings(
            fontSize = 1.4f,
            newShowEn = true,
            newShowKo = false,
            newReadEn = true,
            newReadKo = false,
            order = listOf(Language.KO, Language.EN)
        )

        verify { sharedPrefsEditor.putFloat(ReaderViewModel.PREF_FONT_SIZE_MULTIPLIER, 1.4f) }
        verify { sharedPrefsEditor.putBoolean(ReaderViewModel.PREF_SHOW_EN, true) }
        verify { sharedPrefsEditor.putBoolean(ReaderViewModel.PREF_SHOW_KO, false) }
        verify { sharedPrefsEditor.putBoolean(ReaderViewModel.PREF_READ_EN, true) }
        verify { sharedPrefsEditor.putBoolean(ReaderViewModel.PREF_READ_KO, false) }
        verify { sharedPrefsEditor.putString(ReaderViewModel.PREF_LANGUAGE_ORDER, "KO,EN") }

        assertEquals(1.4f, viewModel.fontSizeMultiplier.value)
        assertEquals(true, viewModel.showEn.value)
        assertEquals(false, viewModel.showKo.value)
        assertEquals(true, viewModel.readEn.value)
        assertEquals(false, viewModel.readKo.value)
        assertEquals(listOf(Language.KO, Language.EN), viewModel.languageOrder.value)
    }

    @Test
    fun languageOrder_restoresFromSharedPreferences() {
        val customPrefs = mockk<SharedPreferences>(relaxed = true)
        val customApp = mockk<Application>(relaxed = true)
        every { customApp.getSharedPreferences("ReaderPrefs", Context.MODE_PRIVATE) } returns customPrefs
        every { customApp.getSystemService(Context.AUDIO_SERVICE) } returns audioManager
        every { customPrefs.getString(ReaderViewModel.PREF_LANGUAGE_ORDER, null) } returns "KO,EN"
        every { customPrefs.getFloat(ReaderViewModel.PREF_FONT_SIZE_MULTIPLIER, 1.0f) } returns 1.5f

        val customVm = ReaderViewModel(customApp, viewModel.bookConfig, ttsManager, billingManager)
        assertEquals(listOf(Language.KO, Language.EN), customVm.languageOrder.value)
        assertEquals(1.5f, customVm.fontSizeMultiplier.value)
    }

    @Test
    fun audioFocus_lossTransientCanDuck_pausesPlayback_andResumesOnGain() {
        val isPlayingField = ReaderViewModel::class.java.getDeclaredField("_isPlaying")
        isPlayingField.isAccessible = true
        @Suppress("UNCHECKED_CAST")
        (isPlayingField.get(viewModel) as MutableStateFlow<Boolean>).value = true
        viewModel.hasAudioFocus = true

        seedQueue(enSentence, index = 0)

        // Simulate Android Auto navigation speaking (AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK)
        viewModel.audioFocusChangeListener.onAudioFocusChange(AudioManager.AUDIOFOCUS_LOSS_TRANSIENT_CAN_DUCK)

        assertFalse("Playback must pause during navigation prompt", viewModel.isPlaying.value)
        assertTrue("wasPlayingBeforeFocusLoss should be true for auto-resumption", viewModel.wasPlayingBeforeFocusLoss)
        verify { ttsManager.stop() }

        // Simulate navigation prompt finishing (AUDIOFOCUS_GAIN)
        viewModel.audioFocusChangeListener.onAudioFocusChange(AudioManager.AUDIOFOCUS_GAIN)
        assertFalse("wasPlayingBeforeFocusLoss should be reset", viewModel.wasPlayingBeforeFocusLoss)
        assertTrue("hasAudioFocus should be true", viewModel.hasAudioFocus)
        assertTrue("Playback should resume after navigation prompt finishes", viewModel.isPlaying.value)
    }

    @Test
    fun audioFocus_lossPermanent_pausesPlayback_andDoesNotResumeOnGain() {
        val isPlayingField = ReaderViewModel::class.java.getDeclaredField("_isPlaying")
        isPlayingField.isAccessible = true
        @Suppress("UNCHECKED_CAST")
        (isPlayingField.get(viewModel) as MutableStateFlow<Boolean>).value = true
        viewModel.hasAudioFocus = true

        // Simulate permanent audio focus loss (e.g. user starts Spotify or YouTube)
        viewModel.audioFocusChangeListener.onAudioFocusChange(AudioManager.AUDIOFOCUS_LOSS)

        assertFalse("Playback must pause on permanent loss", viewModel.isPlaying.value)
        assertFalse("wasPlayingBeforeFocusLoss must be false on permanent loss", viewModel.wasPlayingBeforeFocusLoss)
        assertFalse("hasAudioFocus must be false", viewModel.hasAudioFocus)

        // Subsequent gain from another app finishing should NOT resume reading
        viewModel.audioFocusChangeListener.onAudioFocusChange(AudioManager.AUDIOFOCUS_GAIN)
        assertFalse("Playback must not auto-resume after permanent loss", viewModel.isPlaying.value)
    }

    @Test
    fun playOrPause_whenPlaying_abandonsAudioFocus() {
        val isPlayingField = ReaderViewModel::class.java.getDeclaredField("_isPlaying")
        isPlayingField.isAccessible = true
        @Suppress("UNCHECKED_CAST")
        (isPlayingField.get(viewModel) as MutableStateFlow<Boolean>).value = true
        viewModel.hasAudioFocus = true

        viewModel.playOrPause()

        assertFalse(viewModel.isPlaying.value)
        assertFalse(viewModel.hasAudioFocus)
    }
    /** Seed the sentence queue directly; callers must have settled any chapter load. */
    private fun seedQueue(vararg sentences: com.tkprof.shared.model.Sentence, index: Int) {
        val queueField = ReaderViewModel::class.java.getDeclaredField("sentenceQueue")
        queueField.isAccessible = true
        queueField.set(viewModel, sentences.toList())
        val indexField = ReaderViewModel::class.java.getDeclaredField("currentQueueIndex")
        indexField.isAccessible = true
        indexField.set(viewModel, index)
    }

    private fun currentQueueIndex(): Int {
        val indexField = ReaderViewModel::class.java.getDeclaredField("currentQueueIndex")
        indexField.isAccessible = true
        return indexField.get(viewModel) as Int
    }

    private val enSentence = com.tkprof.shared.model.Sentence("1_EN_0", "Hello world", Language.EN, 1, 0, 11)
    private val koSentence = com.tkprof.shared.model.Sentence("1_KO_0", "\uc548\ub155\ud558\uc138\uc694", Language.KO, 1, 0, 5)

    @Test
    fun playOrPause_withBothLanguagesMuted_staysOnTheChapter() {
        // Regression: muting both languages made every sentence "skip", which ran off
        // the end of the queue and loaded the next chapter, then the next, carrying
        // the reader to the end of the book without ever speaking.
        isFullUnlockedFlow.value = true
        viewModel.readEn.value = false
        viewModel.readKo.value = false
        seedQueue(enSentence, koSentence, index = 0)

        val chapterBefore = viewModel.currentChapterNumber.value
        viewModel.playOrPause()

        assertEquals("Play must not change chapter when nothing is readable", chapterBefore, viewModel.currentChapterNumber.value)
        assertFalse("Play must not report playing when nothing is readable", viewModel.isPlaying.value)
        verify(exactly = 0) { ttsManager.speakEnglish(any(), any(), any()) }
        verify(exactly = 0) { ttsManager.speakKorean(any(), any(), any()) }
    }

    @Test
    fun canRead_isFalse_onlyWhenBothLanguagesAreMuted() {
        viewModel.readEn.value = false
        viewModel.readKo.value = true
        assertTrue(viewModel.readEn.value || viewModel.readKo.value)

        viewModel.readKo.value = false
        assertFalse(viewModel.readEn.value || viewModel.readKo.value)
    }

    @Test
    fun playCurrentSequence_withStaleIndex_resyncsInsteadOfChangingChapter() {
        // Regression: an index left over from a longer chapter read as "past the end"
        // and silently advanced the chapter.
        isFullUnlockedFlow.value = true
        seedQueue(enSentence, koSentence, index = 57)

        val chapterBefore = viewModel.currentChapterNumber.value
        viewModel.playOrPause()

        assertEquals("A stale index must not change chapter", chapterBefore, viewModel.currentChapterNumber.value)
        assertTrue("Index must be brought back inside the queue", currentQueueIndex() in 0..1)
    }

    @Test
    fun previousSentence_withNothingSelected_staysOnTheChapter() {
        // Regression: with no sentence selected the backward scan started at -2, found
        // nothing, and fell through to loading the previous chapter.
        isFullUnlockedFlow.value = true
        viewModel.loadChapter(4, autoPlay = false, selectOnLoad = false)
        awaitChapterLoad()
        seedQueue(enSentence, koSentence, index = -1)

        viewModel.previousSentence()

        assertEquals("Previous must not leave the chapter when nothing is selected", 4, viewModel.currentChapterNumber.value)
    }
}
