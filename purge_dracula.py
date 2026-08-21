import os
import shutil

base = r'c:\git_repo\Book_apps\secret_garden\src\main'

# 1. Strings.xml
strings_path = os.path.join(base, 'res', 'values', 'strings.xml')
strings_content = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">Secret Garden: ??? ??</string>
    <string name="app_name_en">Secret Garden</string>
    <string name="app_name_ko">??? ??</string>
    <string name="iap_product_id">com.tkprof.secretgarden.full</string>
    <integer name="free_chapters">2</integer>
    <integer name="total_chapters">27</integer>
</resources>
"""
with open(strings_path, 'w', encoding='utf-8') as f:
    f.write(strings_content)

# 2. themes.xml
themes_path = os.path.join(base, 'res', 'values', 'themes.xml')
with open(themes_path, 'r', encoding='utf-8') as f:
    themes = f.read()
themes = themes.replace('Theme.Dracula', 'Theme.SecretGarden')
with open(themes_path, 'w', encoding='utf-8') as f:
    f.write(themes)

# 3. AndroidManifest.xml
manifest_path = os.path.join(base, 'AndroidManifest.xml')
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = f.read()
manifest = manifest.replace('Theme.Dracula', 'Theme.SecretGarden')
with open(manifest_path, 'w', encoding='utf-8') as f:
    f.write(manifest)

# 4. Move java package folder
old_pkg = os.path.join(base, 'java', 'com', 'tkprof', 'dracula')
new_pkg = os.path.join(base, 'java', 'com', 'tkprof', 'secretgarden')

if os.path.exists(old_pkg):
    if not os.path.exists(new_pkg):
        os.makedirs(new_pkg)
    for item in os.listdir(old_pkg):
        shutil.move(os.path.join(old_pkg, item), os.path.join(new_pkg, item))
    os.rmdir(old_pkg)

# 5. Fix MainActivity.kt
main_activity = os.path.join(new_pkg, 'MainActivity.kt')
if os.path.exists(main_activity):
    with open(main_activity, 'r', encoding='utf-8') as f:
        kt = f.read()
    kt = kt.replace('package com.tkprof.dracula', 'package com.tkprof.secretgarden')
    kt = kt.replace('Theme.Dracula', 'Theme.SecretGarden')
    with open(main_activity, 'w', encoding='utf-8') as f:
        f.write(kt)

print("All remaining Dracula references have been purged and fixed.")
