from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path).convert('L')
pixels = img.load()

for y in range(480, 520):
    row = ""
    for x in range(490, 530, 2):
        row += "#" if pixels[x, y] > 100 else "."
    print(f"{y}: {row}")
