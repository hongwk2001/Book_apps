import os
from PIL import Image, ImageDraw

def get_bezier_points(p0, p1, p2, steps=50):
    points = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t)**2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
        y = (1 - t)**2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
        points.append((x, y))
    return points

def draw_frankenstein_vector(final_width, final_height, is_feature_graphic=False):
    bg_color = (48, 40, 100) # tkprof_purple
    
    # 8x Supersampling to eliminate all aliasing noise
    ss = 8
    width = final_width * ss
    height = final_height * ss
    
    img = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    if is_feature_graphic:
        scale = (height * 0.7) / 108.0
    else:
        scale = (width * 0.7) / 108.0

    offset_x = (width - 108 * scale) / 2
    offset_y = (height - 108 * scale) / 2
    
    def transform(x, y):
        return (x * scale + offset_x, y * scale + offset_y)
        
    stroke_width = int(8 * scale)
    
    # Quadratic curve
    p0 = transform(24, 70)
    p1 = transform(54, 38)
    p2 = transform(84, 38)
    
    # Use more steps for the larger canvas
    curve_points = get_bezier_points(p0, p1, p2, steps=400)
    
    # Instead of joint='curve', we draw the line normally,
    # but to completely eliminate gaps, we draw a circle at each point.
    r = stroke_width / 2
    for px, py in curve_points:
        draw.ellipse((px-r, py-r, px+r, py+r), fill="white")
        
    # Stitches
    stitches = [
        (35, 48, 45, 64),
        (52, 38, 60, 54),
        (68, 31, 76, 47)
    ]
    
    for sx1, sy1, sx2, sy2 in stitches:
        sp1 = transform(sx1, sy1)
        sp2 = transform(sx2, sy2)
        draw.line([sp1, sp2], fill="white", width=stroke_width)
        draw.ellipse((sp1[0]-r, sp1[1]-r, sp1[0]+r, sp1[1]+r), fill="white")
        draw.ellipse((sp2[0]-r, sp2[1]-r, sp2[0]+r, sp2[1]+r), fill="white")

    # Downscale using Lanczos for perfect anti-aliasing
    final_img = img.resize((final_width, final_height), Image.Resampling.LANCZOS)
    return final_img

out_dir = r'C:\git_repo\Book_apps\play_store_assets\frankenstein'
os.makedirs(out_dir, exist_ok=True)

icon = draw_frankenstein_vector(512, 512, False)
icon.save(os.path.join(out_dir, 'play_store_icon.png'))

fg = draw_frankenstein_vector(1024, 500, True)
fg.save(os.path.join(out_dir, 'feature_graphic.png'))

print("Frankenstein assets generated based on exact XML vector!")
