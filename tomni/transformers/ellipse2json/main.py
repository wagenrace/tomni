import uuid
from typing import Union

# Optimized by chatGDP
def ellipse2json(
    x: int, y: int, radius: int, secondRadius: Union[None, int] = None, alpha: float = 0
) -> dict:
    return {
        "type": "ellipse",
        "center": {"x": int(x), "y": int(y)},
        "radiusX": int(radius),
        "radiusY": int(secondRadius) if secondRadius else int(radius),
        "angleOfRotation": alpha,
        "id": str(uuid.uuid4()),
    }
