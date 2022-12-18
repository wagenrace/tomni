# Chat API generated from unit test
# `can you write python code convert_color function so it passed these unit test:`
import cv2


def convert_color(img, mode):
    # Convert input mode to OpenCV color conversion code
    if mode == "grey" or mode == 1:
        code = cv2.COLOR_BGR2GRAY
    elif mode == "gray" or mode == 2:
        code = cv2.COLOR_BGRA2GRAY
    elif mode == "color" or mode == 3:
        code = cv2.COLOR_GRAY2BGR
    elif mode == "BGr" or mode == 4:
        code = cv2.COLOR_BGRA2BGR
    else:
        raise ValueError(f"{mode} is not a supported color mode")

    # Convert image to desired color space
    img = cv2.cvtColor(img, code)

    return img
