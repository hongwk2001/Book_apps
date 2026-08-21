import re

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('dependencies {', 'dependencies {\n    androidTestImplementation("androidx.test.ext:junit:1.1.5")\n    androidTestImplementation("androidx.test:runner:1.5.2")')

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'w', encoding='utf-8') as f:
    f.write(text)
