import math


def rotate_json(input_json, angle, img_size):
    angle = angle % 360
    center_x = input_json["center"]["x"]
    center_y = input_json["center"]["y"]
    img_width, img_height = img_size

    if input_json["type"] == "ellipse":
        input_json["angleOfRotation"] = (input_json["angleOfRotation"] + angle) % 360
        input_json["center"]["x"] = center_x * math.cos(angle) - center_y * math.sin(
            angle
        )
        input_json["center"]["y"] = center_x * math.sin(angle) + center_y * math.cos(
            angle
        )
        return input_json

    elif input_json["type"] == "polygon":
        rotated_points = []
        for point in input_json["points"]:
            x = point["x"]
            y = point["y"]
            rotated_x = x * math.cos(angle) - y * math.sin(angle)
            rotated_y = x * math.sin(angle) + y * math.cos(angle)
            rotated_points.append({"x": rotated_x, "y": rotated_y})
