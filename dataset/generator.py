from PIL import Image
from PIL import ImageDraw
import random
import math

# https://stackoverflow.com/questions/23411688/drawing-polygon-with-n-number-of-sides-in-python-3-2
def polygon(sides, radius=1, rotation=0, start_coord=(0, 0)):
    one_segment = math.pi * 2 / sides
    points = [(math.sin(one_segment * i + rotation) * radius, math.cos(one_segment * i + rotation) * radius) for i in range(sides)]
    points = [(point[0]+start_coord[0], point[1]+start_coord[1]) for point in points]
    return points

def generate_figure(w, h):
    out_image = Image.new("RGBA", (w, h))

    num_polygons = random.randrange(5, 8)
    for i in range(num_polygons):
        # Immagine con il nuovo poligono
        image = Image.new("RGBA", (w, h))
        draw = ImageDraw.Draw(image)

        points = polygon(
            sides = random.randrange(3, 10), 
            radius = random.randrange(int(w/80), int(w/3)), 
            rotation = random.randrange(0, 359),
            start_coord = (random.randrange(0, w), random.randrange(0, h))
        )

        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 150)
        draw.polygon((points), fill=color)

        # Sovrapposizione delle immagini
        out_image = Image.alpha_composite(out_image, image)

    return out_image.convert("L")

image = generate_figure(512, 512)
image.show()
image.save("test.png")