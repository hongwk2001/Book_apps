import os
import re
import shutil

base = r'c:\git_repo\Book_apps\frankenstein'

# 1. build.gradle.kts
build_gradle = os.path.join(base, 'build.gradle.kts')
with open(build_gradle, 'r', encoding='utf-8') as f:
    bg = f.read()
bg = bg.replace('com.tkprof.secretgarden', 'com.tkprof.frankenstein')
with open(build_gradle, 'w', encoding='utf-8') as f:
    f.write(bg)

# 2. strings.xml
strings_xml = os.path.join(base, 'src', 'main', 'res', 'values', 'strings.xml')
with open(strings_xml, 'r', encoding='utf-8') as f:
    sx = f.read()
sx = sx.replace('Secret Garden', 'Frankenstein')
sx = sx.replace('비밀의 화원', '프랑켄슈타인')
sx = sx.replace('com.tkprof.secretgarden', 'com.tkprof.frankenstein')
sx = re.sub(r'<integer name="total_chapters">.*?</integer>', '<integer name="total_chapters">28</integer>', sx)
with open(strings_xml, 'w', encoding='utf-8') as f:
    f.write(sx)

# 3. themes.xml
themes_xml = os.path.join(base, 'src', 'main', 'res', 'values', 'themes.xml')
with open(themes_xml, 'r', encoding='utf-8') as f:
    tx = f.read()
tx = tx.replace('Theme.SecretGarden', 'Theme.Frankenstein')
with open(themes_xml, 'w', encoding='utf-8') as f:
    f.write(tx)

# 4. AndroidManifest.xml
manifest = os.path.join(base, 'src', 'main', 'AndroidManifest.xml')
with open(manifest, 'r', encoding='utf-8') as f:
    mx = f.read()
mx = mx.replace('Theme.SecretGarden', 'Theme.Frankenstein')
with open(manifest, 'w', encoding='utf-8') as f:
    f.write(mx)

# 5. Move package
old_pkg = os.path.join(base, 'src', 'main', 'java', 'com', 'tkprof', 'secretgarden')
new_pkg = os.path.join(base, 'src', 'main', 'java', 'com', 'tkprof', 'frankenstein')
if os.path.exists(old_pkg):
    os.rename(old_pkg, new_pkg)

# 6. Update MainActivity.kt
main_kt = os.path.join(new_pkg, 'MainActivity.kt')
with open(main_kt, 'r', encoding='utf-8') as f:
    kt = f.read()
kt = kt.replace('package com.tkprof.secretgarden', 'package com.tkprof.frankenstein')
kt = kt.replace('Theme.SecretGarden', 'Theme.Frankenstein')
kt = kt.replace('bookId = "secretgarden"', 'bookId = "frankenstein"')
kt = kt.replace('titleEn = "Secret Garden"', 'titleEn = "Frankenstein"')
kt = kt.replace('titleKo = "비밀의 화원"', 'titleKo = "프랑켄슈타인"')
kt = kt.replace('author = "Frances Hodgson Burnett"', 'author = "Mary Shelley"')
kt = kt.replace('com.tkprof.secretgarden.full', 'com.tkprof.frankenstein.full')
kt = re.sub(r'totalChapters = \d+', 'totalChapters = 28', kt)
with open(main_kt, 'w', encoding='utf-8') as f:
    f.write(kt)

# 7. Empty out assets/books so we don't carry over Secret Garden's json
books_dir = os.path.join(base, 'src', 'main', 'assets', 'books')
for item in os.listdir(books_dir):
    os.remove(os.path.join(books_dir, item))

print("Scaffold config updated successfully.")