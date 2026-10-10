package com.tkprof.shared.tts

// Chinese characters (CJK unified ideographs, extension A, compatibility ideographs).
private const val HANJA = "\\u3400-\\u9FFF\\uF900-\\uFAFF"

// A bracketed note that contains any Chinese character: "(歲)", "(守節冤死 春香之墓)", "(木떡)".
private val HANJA_NOTE = Regex("\\s*\\((?=[^)]*[$HANJA])[^)]*\\)")
private val HANJA_RUN = Regex("[$HANJA]+")
private val SPACE_BEFORE_PUNCT = Regex("\\s+([,.!?;:])")
private val SPACES = Regex("\\s{2,}")

/**
 * The text as it should be spoken. Chinese characters stay on screen (some jokes need
 * to be seen: 女 + 子 = 好), but TTS would read them a second time or in Chinese:
 * "해 세(歲)" became "해 세 세". Bracketed notes holding Chinese characters are dropped,
 * then any bare characters, then the spaces and stray punctuation they leave behind.
 */
fun speakableText(text: String): String {
    if (HANJA_RUN.find(text) == null) return text
    return text
        .replace(HANJA_NOTE, "")
        .replace(HANJA_RUN, "")
        .replace(SPACE_BEFORE_PUNCT, "$1")
        .replace(SPACES, " ")
        .trim()
}
