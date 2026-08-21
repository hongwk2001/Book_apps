import os

res_dir = r'c:\git_repo\Book_apps\dracula\src\main\res'

# 1. Delete all ic_launcher_foreground.png files
for dirpath, dirnames, filenames in os.walk(res_dir):
    for filename in filenames:
        if filename == 'ic_launcher_foreground.png':
            os.remove(os.path.join(dirpath, filename))
            print(f"Deleted {os.path.join(dirpath, filename)}")

# 2. Create Vector XML
vector_content = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    
    <group
        android:translateX="24"
        android:translateY="24"
        android:scaleX="2.5"
        android:scaleY="2.5">
        <path
            android:fillColor="#FFFFFF"
            android:pathData="M0.75,8C0.75,8 5,7 8,9C8,9 8.5,12.75 10.5,12.75V11C10.5,11 11,12 12,12C13,12 13.5,11 13.5,11V12.75C15.5,12.75 16,9 16,9C19,7 23.25,8 23.25,8C21.25,9 21,12.5 21,12.5C17,12.5 17,15.75 17,15.75C12,14.75 12,18.5 12,18.5C12,18.5 12,14.75 7,15.75C7,15.75 7,12.5 3,12.5C3,12.5 2.75,9 0.75,8Z" />
    </group>
</vector>
"""

# 3. Create the XML file in mipmap-anydpi-v26
anydpi_dir = os.path.join(res_dir, 'mipmap-anydpi-v26')
if not os.path.exists(anydpi_dir):
    os.makedirs(anydpi_dir)
with open(os.path.join(anydpi_dir, 'ic_launcher_foreground.xml'), 'w', encoding='utf-8') as f:
    f.write(vector_content)

print("Dracula vector icon created.")
