import os

res_dir = r'c:\git_repo\Book_apps\secret_garden\src\main\res'

# 1. Delete all ic_launcher_foreground.png files
for dirpath, dirnames, filenames in os.walk(res_dir):
    for filename in filenames:
        if filename == 'ic_launcher_foreground.png':
            os.remove(os.path.join(dirpath, filename))

# 2. Create Vector XML
vector_content = """<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    
    <!-- We center the 24x24 icon inside a 108x108 canvas. 
         Scale factor ~ 2.5, translation to center.
         (108 - 24*2.5)/2 = (108 - 60)/2 = 24.
         So we can use a group to scale and translate -->
    <group
        android:translateX="24"
        android:translateY="24"
        android:scaleX="2.5"
        android:scaleY="2.5">
        <path
            android:fillColor="#FFFFFF"
            android:pathData="M12.65,10C11.83,7.67 9.61,6 7,6c-3.31,0 -6,2.69 -6,6s2.69,6 6,6c2.61,0 4.83,-1.67 5.65,-4H17v4h4v-4h2v-4H12.65zM7,14c-1.1,0 -2,-0.9 -2,-2s0.9,-2 2,-2 2,0.9 2,2S8.1,14 7,14z" />
    </group>
</vector>
"""

# 3. Create the XML file in mipmap-anydpi-v26
anydpi_dir = os.path.join(res_dir, 'mipmap-anydpi-v26')
if not os.path.exists(anydpi_dir):
    os.makedirs(anydpi_dir)
with open(os.path.join(anydpi_dir, 'ic_launcher_foreground.xml'), 'w', encoding='utf-8') as f:
    f.write(vector_content)

print("Icon created.")
