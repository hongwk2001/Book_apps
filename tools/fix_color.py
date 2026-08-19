from PIL import Image
import os

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_just_bat_1787157459360.jpg'
img = Image.open(src_path).convert('RGBA')
pixels = img.load()

# Sample the top-left corner, but slightly inwards to avoid any AI white borders.
# The image is 1024x1024. Let's sample at 100, 100.
bg_color = pixels[100, 100]
hex_color = f'#{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}'

res_dir = r'C:\git_repo\Book_apps\dracula\src\main\res'
xml_content = f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">{hex_color}</color>
</resources>
'''
with open(os.path.join(res_dir, 'values', 'ic_launcher_colors.xml'), 'w') as f:
    f.write(xml_content)

print(f'Corrected background color set to {hex_color}')
