package com.tkprof.shared.model

import org.junit.Assert.assertEquals
import org.junit.Test

class SentenceSplitterTest {

    @Test
    fun testKoreanSplitting() {
        val text = "?????. ??? ??????! ? ?????"
        val sentences = SentenceSplitter.split(text, Language.KO, 2)
        
        assertEquals(3, sentences.size)
        assertEquals("?????.", sentences[0].text)
        assertEquals("2_KO_0", sentences[0].id)
    }

    @Test
    fun testEnglishAbbreviation() {
        val text = "To Mrs. Saville, England. Archangel, March 28th."
        val sentences = SentenceSplitter.split(text, Language.EN, 1)
        
        assertEquals(2, sentences.size)
        assertEquals("To Mrs. Saville, England.", sentences[0].text)
        assertEquals("Archangel, March 28th.", sentences[1].text)
    }
}
