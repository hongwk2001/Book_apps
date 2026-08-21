import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

replacement = '''BoxWithConstraints(
                                    modifier = Modifier
                                        .align(Alignment.TopEnd)
                                        .fillMaxHeight()
                                        .padding(end = 4.dp, top = 8.dp, bottom = 8.dp)
                                        .width(4.dp)
                                        .background(MaterialTheme.colorScheme.onSurface.copy(alpha = 0.1f))
                                ) {
                                    val scrollProportion = firstVisible.toFloat() / (totalItems - visibleItems)
                                    val thumbHeightFraction = (visibleItems.toFloat() / totalItems).coerceIn(0.1f, 1f)
                                    val trackHeight = maxHeight
                                    
                                    Box(
                                        modifier = Modifier
                                            .fillMaxWidth()
                                            .fillMaxHeight(thumbHeightFraction)
                                            .offset(y = (trackHeight - (trackHeight * thumbHeightFraction)) * scrollProportion)
                                            .background(MaterialTheme.colorScheme.primary, shape = androidx.compose.foundation.shape.RoundedCornerShape(2.dp))
                                    )
                                }'''

# Find the existing Box that we messed up and replace it.
text = re.sub(r'Box\(\s*modifier = Modifier\s*\.align\(Alignment\.TopEnd\).*?\.background\(MaterialTheme\.colorScheme\.primary, shape = androidx\.compose\.foundation\.shape\.RoundedCornerShape\(2\.dp\)\)\s*\)\s*\}', replacement, text, flags=re.DOTALL)

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'w', encoding='utf-8') as f:
    f.write(text)
