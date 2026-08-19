from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\v4_homescreen_user_bat_fixed.png'
img = Image.open(src_path).convert('RGB')
pixels = img.load()

print("\nIN DOCK (y=2010):")
for x in range(500, 700, 10):
    r,g,b = pixels[x, 2010]
    print(f"x={x}: #{r:02x}{g:02x}{b:02x}")
