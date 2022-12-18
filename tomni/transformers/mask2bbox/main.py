import cv2  # import numpy as np replaced with import cv2

# created from `can you write python code mask2bbox function so it passed these unit tests:`
def mask2bbox(mask, padding):
    """
    Convert a mask to a bounding box.
    Parameters
    ----------
    mask: numpy.ndarray
        Input mask.
    padding: int
        Amount of padding to add to the bounding box.
    Returns
    -------
    tuple
        Bounding box in the format (x, y, width, height).
    """
    x, y, w, h = cv2.boundingRect(mask)
    x -= padding
    y -= padding
    w += 2 * padding
    h += 2 * padding
    return (x, y, w, h)
