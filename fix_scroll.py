import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

old_le = '''                    LaunchedEffect(speakingParagraphIndex) {
                        if (speakingParagraphIndex >= 0) {
                            listState.animateScrollToItem(speakingParagraphIndex)
                        }
                    }'''
                    
new_le = '''                    LaunchedEffect(speakingParagraphIndex, chapter) {
                        if (speakingParagraphIndex >= 0) {
                            kotlinx.coroutines.delay(150)
                            listState.animateScrollToItem(speakingParagraphIndex)
                        }
                    }'''

text = text.replace(old_le, new_le)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
