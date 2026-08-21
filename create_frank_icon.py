import os

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
        <!-- Material Design Lightning Bolt (Flash) -->
        <path
            android:fillColor="#FFFFFF"
            android:pathData="M7,2v11h3v9l7,-12h-4l4,-8z" />
    </group>
</vector>
"""

anydpi_dir = r'c:\git_repo\Book_apps\frankenstein\src\main\res\mipmap-anydpi-v26'
with open(os.path.join(anydpi_dir, 'ic_launcher_foreground.xml'), 'w', encoding='utf-8') as f:
    f.write(vector_content)

print("Created lightning bolt icon.")