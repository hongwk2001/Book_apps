import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('.offset(y = {', '.offset {')
text = text.replace('val availableSpace = this.maxHeight - (this.maxHeight * thumbHeightFraction)\n                                                (availableSpace * scrollProportion).roundToPx()\n                                            })', 'val availableSpace = size.height - (size.height * thumbHeightFraction)\n                                                androidx.compose.ui.unit.IntOffset(0, (availableSpace * scrollProportion).toInt())\n                                            }')

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
