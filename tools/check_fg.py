from PIL import Image

path = r'C:\git_repo\Book_apps\dracula\src\main\res\mipmap-mdpi\ic_launcher_foreground.png'
img = Image.open(path).convert('RGBA')
width, height = img.size
pixels = img.load()

colors = set()
for y in range(0, height, 10):
    for x in range(0, width, 10):
        colors.add(pixels[x, y])

print(f"Colors sampled (RGBA): {colors}")
