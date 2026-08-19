from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\v4_app_drawer_bat.png'
img = Image.open(src_path).convert('RGB')
pixels = img.load()
width, height = img.size

for y in range(0, height, 10):
    for x in range(0, width, 10):
        r,g,b = pixels[x, y]
        if r == 0x13 and g == 0x03 and b == 0x19:
            print(f"Found dark purple at {x}, {y}")
