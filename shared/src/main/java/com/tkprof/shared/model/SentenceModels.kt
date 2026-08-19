package com.tkprof.shared.model

import java.text.BreakIterator
import java.util.Locale

enum class Language { EN, KO }

data class Sentence(
    val id: String, // format: "{paragraphId}_{lang}_{index}"
    val text: String,
    val lang: Language,
    val paragraphId: Int,
    val startIndex: Int, // character offset in the paragraph string
    val endIndex: Int
)

object SentenceSplitter {
    fun split(text: String, lang: Language, paragraphId: Int): List<Sentence> {
        val locale = if (lang == Language.EN) Locale.US else Locale.KOREA
        val iterator = BreakIterator.getSentenceInstance(locale)
        iterator.setText(text)
        
        val sentences = mutableListOf<Sentence>()
        var start = iterator.first()
        var end = iterator.next()
        var index = 0
        
        while (end != BreakIterator.DONE) {
            val sentenceText = text.substring(start, end).trim()
            if (sentenceText.isNotEmpty()) {
                sentences.add(
                    Sentence(
                        id = "${paragraphId}_${lang.name}_$index",
                        text = sentenceText,
                        lang = lang,
                        paragraphId = paragraphId,
                        startIndex = start,
                        endIndex = end
                    )
                )
                index++
            }
            start = end
            end = iterator.next()
        }
        
        // Fallback for very short or un-split text
        if (sentences.isEmpty() && text.isNotBlank()) {
            sentences.add(
                Sentence(
                    id = "${paragraphId}_${lang.name}_0",
                    text = text.trim(),
                    lang = lang,
                    paragraphId = paragraphId,
                    startIndex = 0,
                    endIndex = text.length
                )
            )
        }
        return sentences
    }
}
