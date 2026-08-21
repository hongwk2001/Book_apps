import os

theme_kt = r'c:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\theme\Theme.kt'

content = """package com.tkprof.shared.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFF130319),
    onPrimary = Color.White,
    secondary = Color(0xFF03DAC6),
    background = Color(0xFF121212),
    surface = Color(0xFF1E1E1E),
    primaryContainer = Color(0xFF130319),
    onPrimaryContainer = Color.White
)

private val LightColorScheme = lightColorScheme(
    primary = Color(0xFF130319),
    onPrimary = Color.White,
    secondary = Color(0xFF00BFA5), // Darker teal for light theme secondary
    background = Color(0xFFF8F4F0),
    surface = Color(0xFFFFFFFF),
    primaryContainer = Color(0xFF130319),
    onPrimaryContainer = Color.White
)

@Composable
fun TKProfReaderTheme(
    darkTheme: Boolean = false,
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme
    MaterialTheme(
        colorScheme = colorScheme,
        typography = ReaderTypography,
        content = content
    )
}
"""

with open(theme_kt, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Theme.kt")
