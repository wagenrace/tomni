from typing import List, Union
import copy
from ...transformers import json2contours
from ...contour_operations import get_center
from ..translation import translation_json

# created from `can you write python code crop_json function so it passed these unit tests:`
def crop_json(input_json, x_move, y_move, inputDim):
    output_json = []
    for patch in input_json:
        if patch["type"] == "ellipse":
            x = patch["center"]["x"] - x_move
            y = patch["center"]["y"] - y_move
            if x >= 0 and x < inputDim[0] and y >= 0 and y < inputDim[1]:
                patch["center"]["x"] = x
                patch["center"]["y"] = y
                output_json.append(patch)
        elif patch["type"] == "polygon":
            new_points = []
            for point in patch["points"]:
                x = point["x"] - x_move
                y = point["y"] - y_move
                if x >= 0 and x < inputDim[0] and y >= 0 and y < inputDim[1]:
                    point["x"] = x
                    point["y"] = y
                    new_points.append(point)
            if len(new_points) > 0:
                patch["points"] = new_points
                output_json.append(patch)
    return output_json
