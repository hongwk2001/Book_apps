from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path).convert('L')
pixels = img.load()

# Let's find the bounds of the bat.
# Scan center column from y=300 to 700
for y in range(300, 700):
    if pixels[512, y] > 200:
        print(f"White pixel at y={y}")
