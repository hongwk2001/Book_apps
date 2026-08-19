from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\v4_app_drawer_bat.png'
img = Image.open(src_path).convert('RGB')
pixels = img.load()

# Find the bat icon in the app drawer.
# It is the Dracula app, roughly row 4, column 3.
# Let's search for the #130319 background.

for y in range(1300, 1500, 10):
    for x in range(500, 800, 10):
        r,g,b = pixels[x, y]
        if r < 25 and g < 10 and b < 30: # Dark purple
            print(f"Found dark purple at {x}, {y}: #{r:02x}{g:02x}{b:02x}")

