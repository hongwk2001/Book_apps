from PIL import Image

img_path = r"C:\Users\hongw\.gemini\antigravity\brain\d2ce9842-01e6-483c-ae25-ed74580253c7\.user_uploaded\media_1787248222361.png"
img = Image.open(img_path)
img = img.convert('RGB')
width, height = img.size
x = width // 2
for y in range(20, 35, 2):
    r, g, b = img.getpixel((x, y))
    print(f"y={y}: #{r:02x}{g:02x}{b:02x}")
