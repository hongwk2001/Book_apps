package com.tkprof.shared.model

import kotlinx.serialization.Serializable

/**
 * One aligned paragraph pair. is_header marks chapter titles.
 */
@Serializable
data class BilingualParagraph(
    val id: Int,
    val tag: String? = null,
    val en: String,
    val ko: String,
    val is_header: Boolean = false
)

/**
 * Chapter metadata + its paragraphs.
 * Chapters are loaded lazily (one file per chapter) to keep memory usage low.
 */
@Serializable
data class BilingualChapter(
    val chapterNumber: Int,
    val titleEn: String,
    val titleKo: String,
    val paragraphs: List<BilingualParagraph>
)

/**
 * Lightweight book config — embedded in the app as a constant rather than JSON,
 * since each app IS one book.
 */
data class BookConfig(
    val bookId: String,         // e.g. "dracula"
    val titleEn: String,
    val titleKo: String,
    val author: String,
    val totalChapters: Int,
    val freeChapters: Int,      // chapters readable without purchase
    val iapProductId: String    // e.g. "com.tkprof.dracula.full"
)
