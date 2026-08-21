import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# Add Rect import
if 'import androidx.compose.ui.geometry.Rect' not in text:
    text = text.replace('import androidx.compose.ui.unit.IntOffset', 'import androidx.compose.ui.unit.IntOffset\nimport androidx.compose.ui.geometry.Rect')

# Update LaunchedEffect
old_effect = '''    LaunchedEffect(speakingId, highlightY) {
        if (sentences.any { it.id == speakingId }) {
            requester.bringIntoView()
        }
    }'''

new_effect = '''    val density = LocalDensity.current
    LaunchedEffect(speakingId, highlightY) {
        if (sentences.any { it.id == speakingId }) {
            // Pad the bounding box by 250dp above and below.
            // This forces the scrolling list to place the sentence near the center of the screen,
            // rather than stopping the moment it barely crosses the bottom edge.
            val padding = with(density) { 250.dp.toPx() }
            requester.bringIntoView(Rect(0f, -padding, 1f, padding))
        }
    }'''

text = text.replace(old_effect, new_effect)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
