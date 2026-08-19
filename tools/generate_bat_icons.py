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
        for folder, size in sizes.items():
            folder_path = os.path.join(res_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Resize image to adaptive icon size
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            
            # Save foreground
            output_path = os.path.join(folder_path, 'ic_launcher_foreground.png')
            resized_img.save(output_path, 'PNG')
            
    print('Adaptive foregrounds (Just Bat) generated successfully!')
except Exception as e:
    print(f'Error generating icons: {e}')
