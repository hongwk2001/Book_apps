from PIL import Image
import os

src_path = r'C:\git_repo\Book_apps\tools\bat_extracted.png'
bat_only = Image.open(src_path).convert('RGBA')

sizes = {
    'mipmap-mdpi': 108,
    'mipmap-hdpi': 162,
    'mipmap-xhdpi': 216,
    'mipmap-xxhdpi': 324,
    'mipmap-xxxhdpi': 432
}
res_dir = r'C:\git_repo\Book_apps\dracula\src\main\res'

for folder, size in sizes.items():
    folder_path = os.path.join(res_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    fg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # Scale bat to be exactly 50% of the total adaptive icon canvas
    bat_target_width = int(size * 0.50)
    aspect = bat_only.height / bat_only.width
    bat_target_height = int(bat_target_width * aspect)
    
    resized_bat = bat_only.resize((bat_target_width, bat_target_height), Image.Resampling.LANCZOS)
    
    offset_x = (size - bat_target_width) // 2
    offset_y = (size - bat_target_height) // 2
    
    fg.paste(resized_bat, (offset_x, offset_y), resized_bat)
    fg.save(os.path.join(folder_path, 'ic_launcher_foreground.png'), 'PNG')

# Set the background layer to the exact solid hex color
xml_content = '''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">#160227</color>
</resources>
'''
with open(os.path.join(res_dir, 'values', 'ic_launcher_colors.xml'), 'w') as f:
    f.write(xml_content)

print('Adaptive icons generated!')
