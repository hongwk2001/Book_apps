import re

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('dependencies {', 'dependencies {\n    implementation("androidx.media:media:1.7.0")')

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'w', encoding='utf-8') as f:
    f.write(text)
