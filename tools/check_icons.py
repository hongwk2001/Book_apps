from PIL import Image

path = r'C:\git_repo\Book_apps\dracula\src\main\res\mipmap-mdpi\ic_launcher.png'
img = Image.open(path).convert('RGBA')
print(f"ic_launcher.png size: {img.size}")

path_fg = r'C:\git_repo\Book_apps\dracula\src\main\res\mipmap-mdpi\ic_launcher_foreground.png'
img_fg = Image.open(path_fg).convert('RGBA')
print(f"ic_launcher_foreground.png size: {img_fg.size}")
