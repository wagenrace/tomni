import numpy as np

from ..annotation import Annotation
from ..point import Point


class Ellipse(Annotation):
    def __init__(self, radius: Point, center: Point, rotation: float):
        self._radius: Point = radius
        self._center: Point = center
        self._rotation: float = rotation

        self._circularity = None
        self._area = None
        self._perimeter = None
        self._aspect_ratio = None

    @property
    def radius(self) -> Point:
        return self._radius

    @property
    def center(self) -> Point:
        return self._center

    @property
    def rotation(self) -> float:
        return self._rotation

    @property
    def circularity(self) -> float:
        """Circularity described by 4 * pi * Area / Perimeter**2.

        Returns:
            float: Ellipse's circularity.
        """
        if not self._circularity:
            self._calculate_circularity()

        return self._circularity

    @property
    def area(self) -> float:
        """Area described by pi * radiusX * radiusY.

        Returns:
            float: Ellipse's area.
        """
        if not self._area:
            self._calculate_area()

        return self._area

    @property
    def perimeter(self) -> float:
        """Perimeter described by 2*pi*sqrt((radiusX**2 + radiusY**2) / 2).

        Returns:
            float: Ellipse's perimeter.
        """
        if not self._perimeter:
            self._calculate_perimeter()

        return self._perimeter

    @property
    def aspect_ratio(self) -> float:
        """Ratio between minor and major axis in this case radiusX * 2 / radiusY * 2.

        Returns:
            float: Ellipse's aspect ratio.
        """
        if not self._aspect_ratio:
            self._calculate_aspect_ratio()

        return self._aspect_ratio

    def _calculate_circularity(self) -> None:
        self._circularity = 4 * np.pi * self.area / self.perimeter ** 2

    def _calculate_perimeter(self) -> None:
        self._perimeter = (
            2 * np.pi * np.sqrt((self._radius.x ** 2 + self._radius.y ** 2) / 2)
        )

    def _calculate_area(self) -> None:
        self._area = np.pi * self._radius.x * self._radius.y

    def _calculate_aspect_ratio(self) -> None:
        if self._radius.x == self._radius.y:
            self._aspect_ratio = 1.0
        elif self._radius.x > self._radius.y:
            self._aspect_ratio = self._radius.y / self._radius.x
        else:
            self._aspect_ratio = self._radius.x / self._radius.y
