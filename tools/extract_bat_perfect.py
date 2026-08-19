from PIL import Image

src_path = r'C:\git_repo\Book_apps\tools\center.png'
img = Image.open(src_path).convert('RGBA')
width, height = img.size
pixels = img.load()

# Find the bat by starting at its center. 
# We know it's at roughly x=200, y=100 in the 400x400 image.
# Actually, looking at the image, the bat's center is x=200, y=150.
# Let's just scan for white pixels between y=50 and y=200.
# Any white pixel that is contiguous with the bat.
# We will use a simple flood fill algorithm.

def flood_fill_bat():
    visited = set()
    queue = []
    
    # Find a white pixel to start
    for y in range(50, 200):
        if sum(pixels[200, y][:3]) > 600:
            queue.append((200, y))
            break

    while queue:
        x, y = queue.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Check neighbors
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                if (nx, ny) not in visited:
                    r, g, b, _ = pixels[nx, ny]
                    if r > 100 and g > 100 and b > 100:
                        queue.append((nx, ny))
    return visited

bat_pixels = flood_fill_bat()

# Now create a new transparent image and only copy the bat pixels
bat_only = Image.new('RGBA', (width, height), (0,0,0,0))
new_pixels = bat_only.load()

# Calculate bounding box
min_x, max_x = width, 0
min_y, max_y = height, 0

for x, y in bat_pixels:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    
    # We want smooth edges. The flood fill only found pixels > 100.
    # To get perfect smooth edges, we should include a 1-pixel border or just copy the alpha from grayscale.
    # For now, let's just copy the original RGB and set alpha.

# Let's do a better smooth extraction.
# We know the bounding box!
bat_box = (min_x, min_y, max_x, max_y)
print(f"Bat bounding box in center.png: {bat_box}")

# Create final image cropped to bat
final_bat = Image.new('RGBA', (max_x - min_x + 1, max_y - min_y + 1), (0,0,0,0))
final_pixels = final_bat.load()

for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        if (x, y) in bat_pixels:
            r, g, b, a = pixels[x, y]
            # Map 100-255 to alpha 0-255 roughly for smooth edges
            alpha = int((r - 100) * (255.0 / 155.0))
            if alpha > 255: alpha = 255
            if alpha < 0: alpha = 0
            final_pixels[x - min_x, y - min_y] = (255, 255, 255, alpha)

final_bat.save(r'C:\git_repo\Book_apps\tools\bat_extracted.png')
print("Saved bat_extracted.png")
