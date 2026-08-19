from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path).convert('L')
pixels = img.load()

for y in range(400, 550, 5):
    row = ""
    for x in range(350, 650, 10):
        row += "#" if pixels[x, y] > 100 else "."
    print(f"{y:03d}: {row}")
