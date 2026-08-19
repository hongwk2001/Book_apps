import os
from PIL import Image

src_path = r'C:\git_repo\TKprof_book\books\dracula\covers\cover_eng_ko_square.jpg'
res_dir = r'C:\git_repo\Book_apps\dracula\src\main\res'

sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

try:
    with Image.open(src_path) as img:
        for folder, size in sizes.items():
            folder_path = os.path.join(res_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
            output_path = os.path.join(folder_path, 'ic_launcher.png')
            
            # Save standard icon
            resized_img.save(output_path, 'PNG')
            
            # Save round icon (just duplicating standard for now to satisfy manifest)
            output_round_path = os.path.join(folder_path, 'ic_launcher_round.png')
            resized_img.save(output_round_path, 'PNG')
            
    print('Icons generated successfully!')
except Exception as e:
    print(f'Error generating icons: {e}')
