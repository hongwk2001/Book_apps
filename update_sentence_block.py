import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Add imports
imports = '''import androidx.compose.ui.unit.sp
import androidx.compose.foundation.relocation.BringIntoViewRequester
import androidx.compose.foundation.relocation.bringIntoViewRequester
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.IntOffset'''

text = text.replace('import androidx.compose.ui.unit.sp', imports)

# Replace SentenceBlock
old_block = '''private fun SentenceBlock(
    text: String,
    lang: Language,
    paragraphId: Int,
    speakingId: String?,
    textColor: Color,
    fontSizeMultiplier: Float,
    onClick: (String) -> Unit
) {
    val highlightColor = MaterialTheme.colorScheme.primaryContainer
    
    val sentences = remember(text) { SentenceSplitter.split(text, lang, paragraphId) }
    
    val annotatedString = buildAnnotatedString {
        sentences.forEach { s ->
            val isHighlighted = s.id == speakingId
            val start = length
            append(s.text + " ")
            val end = length
            
            addStringAnnotation(tag = "SENTENCE", annotation = s.id, start = start, end = end)
            addStyle(style = SpanStyle(color = textColor, background = if (isHighlighted) highlightColor else Color.Transparent), start = start, end = end)
        }
    }

    ClickableText(
        text = annotatedString,
        style = MaterialTheme.typography.bodyLarge.copy(lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (16 * fontSizeMultiplier).sp),
        onClick = { offset ->
            annotatedString.getStringAnnotations(tag = "SENTENCE", start = offset, end = offset).firstOrNull()?.let {
                onClick(it.item)
            }
        }
    )
}'''

new_block = '''private fun SentenceBlock(
    text: String,
    lang: Language,
    paragraphId: Int,
    speakingId: String?,
    textColor: Color,
    fontSizeMultiplier: Float,
    onClick: (String) -> Unit
) {
    val highlightColor = MaterialTheme.colorScheme.primaryContainer
    
    val sentences = remember(text) { SentenceSplitter.split(text, lang, paragraphId) }
    
    val requester = remember { BringIntoViewRequester() }
    var highlightY by remember { mutableFloatStateOf(0f) }
    
    val annotatedString = buildAnnotatedString {
        sentences.forEach { s ->
            val isHighlighted = s.id == speakingId
            val start = length
            append(s.text + " ")
            val end = length
            
            addStringAnnotation(tag = "SENTENCE", annotation = s.id, start = start, end = end)
            addStyle(style = SpanStyle(color = textColor, background = if (isHighlighted) highlightColor else Color.Transparent), start = start, end = end)
        }
    }

    Box {
        ClickableText(
            text = annotatedString,
            style = MaterialTheme.typography.bodyLarge.copy(lineHeight = (26 * fontSizeMultiplier).sp, fontSize = (16 * fontSizeMultiplier).sp),
            onTextLayout = { layoutResult ->
                val annotation = annotatedString.getStringAnnotations("SENTENCE", 0, annotatedString.length)
                    .firstOrNull { it.item == speakingId }
                if (annotation != null) {
                    val rect = layoutResult.getBoundingBox(annotation.start)
                    highlightY = rect.top
                }
            },
            onClick = { offset ->
                annotatedString.getStringAnnotations(tag = "SENTENCE", start = offset, end = offset).firstOrNull()?.let {
                    onClick(it.item)
                }
            }
        )
        
        Spacer(
            modifier = Modifier
                .padding(top = with(LocalDensity.current) { highlightY.toDp() })
                .size(1.dp)
                .bringIntoViewRequester(requester)
        )
    }
    
    LaunchedEffect(speakingId, highlightY) {
        if (sentences.any { it.id == speakingId }) {
            requester.bringIntoView()
        }
    }
}'''

text = text.replace(old_block, new_block)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
