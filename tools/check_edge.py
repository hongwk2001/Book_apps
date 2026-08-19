from PIL import Image

path = r'C:\git_repo\Book_apps\dracula\src\main\res\mipmap-mdpi\ic_launcher_foreground.png'
img = Image.open(path).convert('RGBA')
width, height = img.size
pixels = img.load()

bat_center_x, bat_center_y = width // 2, height // 2
edge_pixels = 0
for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        if a > 0:
            dist = ((x - bat_center_x)**2 + (y - bat_center_y)**2)**0.5
            if dist > 40:
                edge_pixels += 1

print(f"Edge pixels > 40 dist: {edge_pixels}")
