package com.tkprof.shared.data

import android.content.Context
import com.tkprof.shared.model.BilingualChapter
import com.tkprof.shared.model.BilingualParagraph
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

/**
 * Raw paragraph format stored in assets (matches merge_bilingual.py output).
 */
@Serializable
private data class RawParagraph(
    val id: Int,
    val en: String,
    val ko: String,
    val is_header: Boolean = false
)

/**
 * Loads bilingual chapter JSON files from the app's assets/books/ folder.
 * Each file is named ch_NN.json (e.g. ch_01.json .. ch_27.json).
 *
 * Chapters are loaded on demand to avoid loading the entire book into memory.
 */
class BookRepository(private val context: Context) {

    private val json = Json { ignoreUnknownKeys = true }

    /**
     * Load a single chapter by number (1-based).
     * Returns null if the file does not exist.
     */
    fun loadChapter(chapterNumber: Int): BilingualChapter? {
        val filename = "books/ch_%02d.json".format(chapterNumber)
        return try {
            val raw = context.assets.open(filename).bufferedReader().readText()
            val paragraphs = json.decodeFromString<List<RawParagraph>>(raw)

            // First is_header paragraph (if any) provides the chapter title
            val headerEn = paragraphs.firstOrNull { it.is_header }?.en ?: "Chapter $chapterNumber"
            val headerKo = paragraphs.firstOrNull { it.is_header }?.ko ?: "제${chapterNumber}장"

            BilingualChapter(
                chapterNumber = chapterNumber,
                titleEn = headerEn,
                titleKo = headerKo,
                paragraphs = paragraphs.map {
                    BilingualParagraph(
                        id = it.id,
                        en = it.en,
                        ko = it.ko,
                        is_header = it.is_header
                    )
                }
            )
        } catch (e: Exception) {
            null
        }
    }

    /**
     * Returns the count of available chapter files in assets/books/.
     */
    fun availableChapterCount(): Int {
        val files = context.assets.list("books") ?: return 0
        return files.count { it.matches(Regex("ch_\\d+\\.json")) }
    }
}
