from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\v4_homescreen_user_bat.png'
img = Image.open(src_path).convert('RGB')
pixels = img.load()

# Let's check the color of the pixel just inside the right edge of the icon on the home screen.
# The icon is roughly at x=800, y=1900 (bottom right icon)
# Let's find the bounding box of the icon
# Icon is the bat one. It's the 4th icon in the dock.
# Resolution of the screenshot: 1080 x 2400 usually.
# Let's scan a horizontal line through the icon.
width, height = img.size
print(f"Size: {width}x{height}")

# Center of bottom right icon in dock
# For 1080x2400, dock icons are around y=2000. X=880.
y_scan = 2050
found_icon = False
for x in range(700, 1000):
    r,g,b = pixels[x, y_scan]
    if r > 200 and g > 200 and b > 200: # White bat
        print(f"Bat at {x}")

