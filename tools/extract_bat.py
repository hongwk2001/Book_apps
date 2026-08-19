from PIL import Image
import os

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_just_bat_1787157459360.jpg'
img = Image.open(src_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# 1. Get the exact background color near the bat (center-left) to guarantee it matches
bg_color = pixels[width//4, height//2]
hex_color = f'#{bg_color[0]:02x}{bg_color[1]:02x}{bg_color[2]:02x}'

# 2. Convert to grayscale to find the bat (white pixels)
gray = img.convert('L')
gray_data = gray.load()

min_x, max_x = width, 0
min_y, max_y = height, 0

for y in range(height):
    for x in range(width):
        if gray_data[x,y] > 200: # It's part of the white bat
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

# 3. Create a new image containing JUST the bat with a transparent background
bat_only = Image.new('RGBA', (max_x - min_x + 1, max_y - min_y + 1), (0,0,0,0))
bat_pixels = bat_only.load()

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        val = gray_data[x,y]
        if val > 50: # Soft threshold to preserve smooth anti-aliased edges
            # Map 50-255 to 0-255 alpha
            alpha = int((val - 50) * (255.0 / 205.0))
            bat_pixels[x - min_x, y - min_y] = (255, 255, 255, alpha)

# 4. Generate the exact Android Adaptive Icon sizes
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
    
    # Create the transparent foreground layer
    fg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    
    # Scale bat to be exactly 55% of the total adaptive icon canvas (fits perfectly in the safe zone)
    bat_target_width = int(size * 0.55)
    aspect = bat_only.height / bat_only.width
    bat_target_height = int(bat_target_width * aspect)
    
    resized_bat = bat_only.resize((bat_target_width, bat_target_height), Image.Resampling.LANCZOS)
    
    offset_x = (size - bat_target_width) // 2
    offset_y = (size - bat_target_height) // 2
    
    fg.paste(resized_bat, (offset_x, offset_y), resized_bat)
    fg.save(os.path.join(folder_path, 'ic_launcher_foreground.png'), 'PNG')

# 5. Set the background layer to the exact solid hex color
xml_content = f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="ic_launcher_background">{hex_color}</color>
</resources>
'''
with open(os.path.join(res_dir, 'values', 'ic_launcher_colors.xml'), 'w') as f:
    f.write(xml_content)

print(f'Bat extracted! Background color set to {hex_color}')
