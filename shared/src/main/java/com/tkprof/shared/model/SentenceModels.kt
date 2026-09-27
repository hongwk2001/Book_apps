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
    private val abbreviations = setOf(
        "mr", "mrs", "ms", "dr", "prof", "sr", "jr", "st", "mt", "capt", "col", "gen", "lieut", "sgt", "rev"
    )

    fun split(text: String, lang: Language, paragraphId: Int): List<Sentence> {
        val locale = if (lang == Language.EN) Locale.US else Locale.KOREA
        val iterator = BreakIterator.getSentenceInstance(locale)
        iterator.setText(text)
        
        val initialSentences = mutableListOf<Sentence>()
        var start = iterator.first()
        var end = iterator.next()
        var index = 0
        
        while (end != BreakIterator.DONE) {
            val sentenceText = text.substring(start, end).trim()
            if (sentenceText.isNotEmpty()) {
                initialSentences.add(
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
        
        val mergedSentences = mutableListOf<Sentence>()
        var i = 0
        var newIndex = 0
        while (i < initialSentences.size) {
            var current = initialSentences[i]
            
            while (i + 1 < initialSentences.size) {
                val words = current.text.split(" ")
                val lastWord = words.lastOrNull() ?: ""
                
                if (lastWord.endsWith(".") && lastWord.length > 1) {
                    val wordWithoutDot = lastWord.dropLast(1).lowercase().trim('"', '\'', '“', '‘', '”', '’')
                    val isAbbrev = abbreviations.contains(wordWithoutDot)
                    val isSingleLetterInitial = wordWithoutDot.length == 1 && wordWithoutDot[0].isLetter()
                    if (isAbbrev || isSingleLetterInitial) {
                        val next = initialSentences[i + 1]
                        val combinedText = text.substring(current.startIndex, next.endIndex).trim()
                        current = Sentence(
                            id = "${paragraphId}_${lang.name}_$newIndex",
                            text = combinedText,
                            lang = lang,
                            paragraphId = paragraphId,
                            startIndex = current.startIndex,
                            endIndex = next.endIndex
                        )
                        i++
                        continue
                    }
                }
                break
            }
            
            if (current.id != "${paragraphId}_${lang.name}_$newIndex") {
                current = current.copy(id = "${paragraphId}_${lang.name}_$newIndex")
            }
            mergedSentences.add(current)
            newIndex++
            i++
        }

        // Fallback for very short or un-split text
        if (mergedSentences.isEmpty() && text.isNotBlank()) {
            mergedSentences.add(
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
        return mergedSentences
    }
}
