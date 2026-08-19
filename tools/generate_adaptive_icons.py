import os
from PIL import Image

src_path = r'C:\git_repo\TKprof_book\books\dracula\covers\cover_eng_ko_square.jpg'
res_dir = r'C:\git_repo\Book_apps\dracula\src\main\res'

sizes = {
    'mipmap-mdpi': (108, 72),
    'mipmap-hdpi': (162, 108),
    'mipmap-xhdpi': (216, 144),
    'mipmap-xxhdpi': (324, 216),
    'mipmap-xxxhdpi': (432, 288)
}

try:
    with Image.open(src_path) as img:
        for folder, (bg_size, cover_size) in sizes.items():
            folder_path = os.path.join(res_dir, folder)
            os.makedirs(folder_path, exist_ok=True)
            
            # Resize cover
            resized_cover = img.resize((cover_size, cover_size), Image.Resampling.LANCZOS)
            
            # Create transparent background
            foreground = Image.new('RGBA', (bg_size, bg_size), (0, 0, 0, 0))
            
            # Paste cover in center
            offset = (bg_size - cover_size) // 2
            foreground.paste(resized_cover, (offset, offset))
            
            # Save foreground
            output_path = os.path.join(folder_path, 'ic_launcher_foreground.png')
            foreground.save(output_path, 'PNG')
            
    print('Adaptive foregrounds generated successfully!')
except Exception as e:
    print(f'Error generating icons: {e}')
