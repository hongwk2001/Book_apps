import os
from PIL import Image

def create_assets(src_path, prefix, bg_color):
    out_dir = r'C:\git_repo\Book_apps\play_store_assets'
    os.makedirs(out_dir, exist_ok=True)
    
    # Load source image
    src_img = Image.open(src_path).convert("RGBA")
    pixels = src_img.load()
    width, height = src_img.size
    
    # Extract only the white pixels (ignore black background)
    extracted = Image.new("RGBA", (width, height), (0,0,0,0))
    epixels = extracted.load()
    min_x, min_y = width, height
    max_x, max_y = 0, 0
    
    for y in range(height):
        for x in range(width):
            r,g,b,a = pixels[x,y]
            if r > 100 and g > 100 and b > 100:
                epixels[x,y] = (255, 255, 255, 255)
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                
    # Crop to exactly the shape
    cropped = extracted.crop((min_x, min_y, max_x + 1, max_y + 1))
    
    # --- 1. Hi-Res Icon (512x512) ---
    icon_img = Image.new("RGBA", (512, 512), bg_color)
    target_w = int(512 * 0.65)
    ratio = target_w / float(cropped.width)
    target_h = int(cropped.height * ratio)
    
    resized_icon = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
    paste_x = (512 - target_w) // 2
    paste_y = (512 - target_h) // 2
    icon_img.paste(resized_icon, (paste_x, paste_y), resized_icon)
    
    icon_path = os.path.join(out_dir, f'{prefix}_play_store_icon.png')
    icon_img.save(icon_path)
    
    # --- 2. Feature Graphic (1024x500) ---
    feature_img = Image.new("RGBA", (1024, 500), bg_color)
    fg_target_w = int(1024 * 0.40)
    fg_ratio = fg_target_w / float(cropped.width)
    fg_target_h = int(cropped.height * fg_ratio)
    
    # Ensure it fits within 500 height
    if fg_target_h > 450:
        fg_target_h = 450
        fg_ratio = fg_target_h / float(cropped.height)
        fg_target_w = int(cropped.width * fg_ratio)
        
    resized_fg = cropped.resize((fg_target_w, fg_target_h), Image.Resampling.LANCZOS)
    fg_paste_x = (1024 - fg_target_w) // 2
    fg_paste_y = (500 - fg_target_h) // 2
    feature_img.paste(resized_fg, (fg_paste_x, fg_paste_y), resized_fg)
    
    fg_path = os.path.join(out_dir, f'{prefix}_feature_graphic.png')
    feature_img.save(fg_path)
    
    print(f"Generated {icon_path} and {fg_path}")

# Paths for generated images
frank_src = r'C:\Users\hongw\.gemini\antigravity\brain\b3096751-2aa8-4723-92ad-203a7702f30e\frankenstein_source_lightning_1787340558151.jpg'
sg_src = r'C:\Users\hongw\.gemini\antigravity\brain\b3096751-2aa8-4723-92ad-203a7702f30e\secret_garden_source_1787340232539.jpg'

# Colors (tkprof_purple #302864)
tkprof_purple = (48, 40, 100)

create_assets(frank_src, 'frankenstein', tkprof_purple)
create_assets(sg_src, 'secret_garden', tkprof_purple)
