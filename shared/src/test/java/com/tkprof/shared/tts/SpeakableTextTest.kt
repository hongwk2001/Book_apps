package com.tkprof.shared.tts

import org.junit.Assert.assertEquals
import org.junit.Test

class SpeakableTextTest {

    @Test
    fun `text without Chinese characters is unchanged`() {
        val s = "Playing here and there, we forget how time goes by."
        assertEquals(s, speakableText(s))
    }

    @Test
    fun `bracketed reading is dropped in Korean and English`() {
        assertEquals("이리저리 노닐다 보면 세월 가는 줄 모르니 해 세.",
            speakableText("이리저리 노닐다 보면 세월 가는 줄 모르니 해 세(歲)."))
        assertEquals("Playing here and there, we forget how time goes by: se, years.",
            speakableText("Playing here and there, we forget how time goes by: se, years (歲)."))
    }

    @Test
    fun `mixed and multi-word notes are dropped`() {
        assertEquals("이가 단단해서 목떡을 잘 자셨다.", speakableText("이가 단단해서 목떡(木떡)을 잘 자셨다."))
        assertEquals("비석에는 '수절원사 춘향지묘', 곧",
            speakableText("비석에는 '수절원사 춘향지묘(守節冤死 春香之墓)', 곧"))
    }

    @Test
    fun `bare character leaves no stray space before punctuation`() {
        assertEquals("and you get the character, which means 'love' and 'good.'",
            speakableText("and you get the character 好, which means 'love' and 'good.'"))
    }

    @Test
    fun `brackets without Chinese characters are kept`() {
        val s = "(In Korean, the old words in this book sound like \"ko,\" the word for nose.) 好"
        assertEquals("(In Korean, the old words in this book sound like \"ko,\" the word for nose.)", speakableText(s))
    }
}
