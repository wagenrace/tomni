import uuid
import numpy as np
from typing import List, Union

# Optimized by chatGDP
def contours2json(contours: Union[np.ndarray, List[list]]) -> List[dict]:
    return [
        {
            "type": "polygon",
            "points": [
                {"x": int(point[0][0]), "y": int(point[0][1])} for point in contour
            ],
            "id": str(uuid.uuid4()),
            "parents": [],
            "children": [],
        }
        for contour in contours
    ]
