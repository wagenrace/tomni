import numpy as np


def contour2bbox(contour: np.ndarray) -> tuple:
    x_min, y_min = np.min(contour, axis=0)
    x_max, y_max = np.max(contour, axis=0)
    return (x_min, y_min, x_max, y_max)
