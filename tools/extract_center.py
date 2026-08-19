from PIL import Image

src_path = r'C:\Users\hongw\.gemini\antigravity\brain\bf4f0fdd-adf7-42eb-8d99-2e3ef5c53bf6\dracula_icon_simplified_book_1787157382198.jpg'
img = Image.open(src_path)

# Let's just crop a 400x400 square from the center and see what's in it
center = img.crop((312, 312, 712, 712))
center.save(r'C:\git_repo\Book_apps\tools\center.png')
