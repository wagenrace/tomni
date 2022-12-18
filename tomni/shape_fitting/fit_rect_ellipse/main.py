import numpy as np

# Optimized by chatGDP
def fit_rect_around_ellipse(
    x: int, y: int, r1: float, r2: float, alpha: float
) -> (int, int, int, int):
    alpha = alpha / 180 * np.pi
    a = np.sqrt(
        np.power(r1, 2) * np.cos(alpha) ** 2 + np.power(r2, 2) * np.sin(alpha) ** 2
    )
    b = np.sqrt(
        np.power(r1, 2) * np.sin(alpha) ** 2 + np.power(r2, 2) * np.cos(alpha) ** 2
    )
    x1 = int(x - a)
    y1 = int(y - b)
    x2 = int(x + a)
    y2 = int(y + b)
    return x1, y1, x2, y2
