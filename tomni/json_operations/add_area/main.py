import math

# Created by `can you write python code add_area function so it passed these unit tests:`
def add_area(json_object):
    if json_object["type"] == "polygon":
        # Calculate the area of the polygon using the Shoelace formula
        points = json_object["points"]
        n = len(points)
        area = 0.0
        for i in range(n):
            area += points[i]["x"] * points[(i + 1) % n]["y"]
            area -= points[i]["y"] * points[(i + 1) % n]["x"]
        area = abs(area) / 2
        json_object["area"] = area
    elif json_object["type"] == "circle":
        # Calculate the area of the circle
        radiusX = json_object["radiusX"]
        radiusY = json_object["radiusY"]
        json_object["area"] = math.pi * radiusX * radiusY
    elif json_object["type"] == "ellipse":
        # Calculate the area of the ellipse
        radiusX = json_object["radiusX"]
        radiusY = json_object["radiusY"]
        json_object["area"] = math.pi * radiusX * radiusY
    else:
        raise ValueError("Invalid shape type")
