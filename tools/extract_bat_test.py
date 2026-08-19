from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path).convert('L')
gray_data = img.load()

bat_box = (350, 458, 674, 530)
bat_only = Image.new('RGBA', (bat_box[2] - bat_box[0], bat_box[3] - bat_box[1]), (0,0,0,0))
bat_pixels = bat_only.load()

min_x = bat_box[0]
min_y = bat_box[1]

for y in range(bat_box[1], bat_box[3]):
    for x in range(bat_box[0], bat_box[2]):
        val = gray_data[x,y]
        if val > 50:
            alpha = int((val - 50) * (255.0 / 205.0))
            bat_pixels[x - min_x, y - min_y] = (255, 255, 255, alpha)

# Erase the book which might start at the bottom
# The book center fold is at x=512.
# Let's see if we can just erase the vertical book line.
# Actually, let's just save it first to see.
bat_only.save(r'C:\git_repo\Book_apps\tools\temp_bat.png')
print("Saved temp_bat.png")
