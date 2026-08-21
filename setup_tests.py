import re

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'r', encoding='utf-8') as f:
    text = f.read()

deps = '''dependencies {
    testImplementation("junit:junit:4.13.2")
    testImplementation("org.jetbrains.kotlinx:kotlinx-coroutines-test:1.7.3")
    testImplementation("io.mockk:mockk:1.13.5")
    testImplementation("app.cash.turbine:turbine:1.0.0")'''

text = text.replace('dependencies {', deps)

with open(r'C:\git_repo\Book_apps\shared\build.gradle.kts', 'w', encoding='utf-8') as f:
    f.write(text)
