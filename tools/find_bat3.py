from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path).convert('L')
pixels = img.load()

last_state = False
for y in range(300, 900):
    is_white = pixels[450, y] > 200
    if is_white and not last_state:
        print(f"White starts at y={y}")
    elif not is_white and last_state:
        print(f"White ends at y={y-1}")
    last_state = is_white
