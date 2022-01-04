from PIL import Image
from PIL import ImageDraw
import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Restituisce la lista dei vertici di un poligono fissate alcuni valori
# Fonte: https://stackoverflow.com/questions/23411688/drawing-polygon-with-n-number-of-sides-in-python-3-2
def polygon(sides, radius=1, rotation=0, start_coord=(0, 0)):
    one_segment = math.pi * 2 / sides
    points = [(math.sin(one_segment * i + rotation) * radius, math.cos(one_segment * i + rotation) * radius) for i in range(sides)]
    points = [(point[0]+start_coord[0], point[1]+start_coord[1]) for point in points]
    return points

# Restituisce un'immagine contenente poligoni in scala di grigi normalizzata in [0, 1]
# width, height         Dimensione dell'immagine
# min_poygons           Numero minimo di poligoni generati
# max_polygons          Numero massimo di poligoni generati
# max_polygon_sides     Numero massimo di facce dei poligoni
def generate_image(width, height, min_poygons=3, max_polygons=6, max_polygon_sides=10):
    out_image = Image.new("RGBA", (width, height))
    num_polygons = random.randrange(min_poygons, max_polygons)
    
    for i in range(num_polygons):
        # Immagine che conterrà il nuovo poligono
        image = Image.new("RGBA", (width, height))
        draw = ImageDraw.Draw(image)

        # Generazione punti
        points = polygon(
            sides = random.randrange(3, max_polygon_sides), 
            radius = random.randrange(int(width/60), int(width/3)), 
            rotation = random.randrange(0, 359),
            start_coord = (random.randrange(0, width), random.randrange(0, height))
        )

        # Selezione colore
        color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), 150)
        draw.polygon((points), fill=color)

        # Sovrapposizione delle immagini
        out_image = Image.alpha_composite(out_image, image)

    return out_image.convert("L")
    # return np.array(out_image.convert("L")) / 255  # Immagine in scala di grigi normalizzata in [0, 1]


if __name__ == "__main__":
    image = generate_image(512, 512)
    image.show()
    image.save("image.png")

    # print(np.min(image), np.max(image))
    # plt.imshow(image, cmap="gray")
    # plt.show()
