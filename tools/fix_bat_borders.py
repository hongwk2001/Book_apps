import os
from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_just_bat_1787157459360.jpg'
res_dir = r'C:\git_repo\Book_apps\dracula\src\main\res'

sizes = {
    'mipmap-mdpi': 108,
    'mipmap-hdpi': 162,
    'mipmap-xhdpi': 216,
    'mipmap-xxhdpi': 324,
    'mipmap-xxxhdpi': 432
}

try:
    with Image.open(src_path) as img:
        # The AI generated image likely has white corners because it drew a rounded square.
        # We will crop the center 75% of the image to eliminate the corners, leaving pure purple and the bat.
        width, height = img.size
        margin = int(width * 0.125)
        cropped_img = img.crop((margin, margin, width - margin, height - margin))
        
        for folder, size in sizes.items():
            folder_path = os.path.join(res_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Resize the pure purple/bat image to the full adaptive foreground size
            resized_img = cropped_img.resize((size, size), Image.Resampling.LANCZOS)
            
            # Save foreground
            output_path = os.path.join(folder_path, 'ic_launcher_foreground.png')
            resized_img.save(output_path, 'PNG')
            
    print('Adaptive foregrounds generated without white corners!')
except Exception as e:
    print(f'Error generating icons: {e}')
