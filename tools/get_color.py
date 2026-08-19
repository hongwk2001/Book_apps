from PIL import Image

src_path = r'C:\git_repo\Book_apps\tools\center.png'
img = Image.open(src_path).convert('RGB')
pixels = img.load()
r, g, b = pixels[10, 10]
print(f"#{r:02x}{g:02x}{b:02x}")
