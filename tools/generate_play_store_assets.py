import os
from PIL import Image, ImageOps

# Paths
bat_src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\.user_uploaded\media_1787165184491.png'
out_dir = r'C:\git_repo\Book_apps\play_store_assets'
os.makedirs(out_dir, exist_ok=True)

# Colors
bg_color = (19, 3, 25) # #130319
bat_color = (255, 255, 255)

# Load user image and extract bat (similar to previous extraction)
src_img = Image.open(bat_src_path).convert("RGBA")
pixels = src_img.load()
width, height = src_img.size

# Extract only the white/light pixels
extracted_bat = Image.new("RGBA", (width, height), (0,0,0,0))
epixels = extracted_bat.load()
min_x, min_y = width, height
max_x, max_y = 0, 0

for y in range(height):
    for x in range(width):
        r,g,b,a = pixels[x,y]
        if r > 150 and g > 150 and b > 150:
            epixels[x,y] = (255, 255, 255, 255)
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

# Crop to exactly the bat
bat_cropped = extracted_bat.crop((min_x, min_y, max_x + 1, max_y + 1))

# --- 1. Hi-Res Icon (512x512) ---
# For the icon, Play Store expects 512x512. It will apply its own rounding.
icon_img = Image.new("RGBA", (512, 512), bg_color)
# Calculate scale for bat to fit nicely (say, 60% of the width)
target_w = int(512 * 0.65)
ratio = target_w / float(bat_cropped.width)
target_h = int(bat_cropped.height * ratio)

bat_resized_icon = bat_cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
paste_x = (512 - target_w) // 2
paste_y = (512 - target_h) // 2
icon_img.paste(bat_resized_icon, (paste_x, paste_y), bat_resized_icon)

icon_path = os.path.join(out_dir, 'play_store_icon.png')
icon_img.save(icon_path)

# --- 2. Feature Graphic (1024x500) ---
# A clean dark purple background with the bat centered and slightly larger
feature_img = Image.new("RGBA", (1024, 500), bg_color)
# Make the bat take up about 40% of the width
fg_target_w = int(1024 * 0.40)
fg_ratio = fg_target_w / float(bat_cropped.width)
fg_target_h = int(bat_cropped.height * fg_ratio)

bat_resized_fg = bat_cropped.resize((fg_target_w, fg_target_h), Image.Resampling.LANCZOS)
fg_paste_x = (1024 - fg_target_w) // 2
fg_paste_y = (500 - fg_target_h) // 2
feature_img.paste(bat_resized_fg, (fg_paste_x, fg_paste_y), bat_resized_fg)

fg_path = os.path.join(out_dir, 'feature_graphic.png')
feature_img.save(fg_path)

print(f"Generated {icon_path} and {fg_path}")
