import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ParagraphCard signature
text = re.sub(
    r'private fun ParagraphCard\(\s*paragraph: BilingualParagraph,\s*speakingId: String\?,\s*isEnFirst: Boolean,\s*showEn: Boolean,\s*showKo: Boolean,\s*onSentenceClick: \(String\) -> Unit\s*\)',
    'private fun ParagraphCard(\n    paragraph: BilingualParagraph,\n    speakingId: String?,\n    isEnFirst: Boolean,\n    showEn: Boolean,\n    showKo: Boolean,\n    fontSizeMultiplier: Float,\n    onSentenceClick: (String) -> Unit\n)',
    text
)

# Pass fontSizeMultiplier into SentenceBlock calls inside ParagraphCard
text = re.sub(r'SentenceBlock\((.*?),(.*?),(.*?),(.*?),(.*?),(.*?)\)', r'SentenceBlock(\1,\2,\3,\4,\5, fontSizeMultiplier, \6)', text)

# Add fontSizeMultiplier to SentenceBlock signature
text = re.sub(
    r'private fun SentenceBlock\(\s*text: String,\s*lang: Language,\s*paragraphId: Int,\s*speakingId: String\?,\s*textColor: Color,\s*onClick: \(String\) -> Unit\s*\)',
    'private fun SentenceBlock(\n    text: String,\n    lang: Language,\n    paragraphId: Int,\n    speakingId: String?,\n    textColor: Color,\n    fontSizeMultiplier: Float,\n    onClick: (String) -> Unit\n)',
    text
)

# Use fontSizeMultiplier in ClickableText style
text = re.sub(
    r'style = MaterialTheme.typography.bodyLarge.copy\(lineHeight = 26.sp\)',
    'style = MaterialTheme.typography.bodyLarge.copy(lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (16 * fontSizeMultiplier).sp)',
    text
)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
