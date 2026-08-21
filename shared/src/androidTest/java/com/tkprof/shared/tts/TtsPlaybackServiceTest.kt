package com.tkprof.shared.tts

import android.content.Intent
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class TtsPlaybackServiceTest {
    @Test
    fun testServiceStartsWithoutCrashing() {
        val context = InstrumentationRegistry.getInstrumentation().targetContext
        val intent = Intent(context, TtsPlaybackService::class.java).apply {
            putExtra("BOOK_TITLE", "Test Title")
        }
        
        context.startService(intent)
        Thread.sleep(1000)
    }
}
