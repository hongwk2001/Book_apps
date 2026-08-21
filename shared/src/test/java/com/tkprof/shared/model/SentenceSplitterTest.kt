package com.tkprof.shared.model

import org.junit.Assert.assertEquals
import org.junit.Test

class SentenceSplitterTest {

    @Test
    fun testKoreanSplitting() {
        val text = "?????. ??? ??????! ? ?????"
        val sentences = SentenceSplitter.split(text, Language.KO, 2)
        
        for (i in sentences.indices) {
            println("Sentence $i: '${sentences[i].text}'")
        }
        
        assertEquals(3, sentences.size)
        assertEquals("?????.", sentences[0].text)
        assertEquals("2_KO_0", sentences[0].id)
    }
}
