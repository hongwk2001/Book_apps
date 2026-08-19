from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\.user_uploaded\media_1787165184491.png'
img = Image.open(src_path).convert('RGB')

# Let's sample a few pixels to get the dominant background color
pixels = [
    img.getpixel((5, 5)),
    img.getpixel((10, 10)),
    img.getpixel((img.width - 5, 5)),
    img.getpixel((5, img.height - 5))
]

for p in pixels:
    print(f"RGB: {p}, HEX: #{p[0]:02x}{p[1]:02x}{p[2]:02x}")
