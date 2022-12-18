from unittest import TestCase
import numpy as np
import math
from .main import add_area


class TestAddAreaJson(TestCase):
    def test_happy_flow(self):
        json_object = {
            "type": "polygon",
            "points": [
                {"x": 0, "y": 10},
                {"x": 10, "y": 10},
                {"x": 10, "y": 0},
                {"x": 0, "y": 0},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
        }

        expected_result = {
            "type": "polygon",
            "points": [
                {"x": 0, "y": 10},
                {"x": 10, "y": 10},
                {"x": 10, "y": 0},
                {"x": 0, "y": 0},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
            "area": 100.0,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_triangle(self):
        json_object = {
            "type": "polygon",
            "points": [
                {"x": 0, "y": 10},
                {"x": 10, "y": 10},
                {"x": 0, "y": 0},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
        }

        expected_result = {
            "type": "polygon",
            "points": [
                {"x": 0, "y": 10},
                {"x": 10, "y": 10},
                {"x": 0, "y": 0},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
            "area": 50.0,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_diamond(self):
        json_object = {
            "type": "polygon",
            "points": [
                {"x": 10, "y": 10},
                {"x": 20, "y": 20},
                {"x": 10, "y": 30},
                {"x": 0, "y": 20},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
        }

        expected_result = {
            "type": "polygon",
            "points": [
                {"x": 10, "y": 10},
                {"x": 20, "y": 20},
                {"x": 10, "y": 30},
                {"x": 0, "y": 20},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
            "area": 200.0,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_octagon(self):
        json_object = {
            "type": "polygon",
            "points": [
                {"x": 10, "y": 10},
                {"x": 20, "y": 10},
                {"x": 30, "y": 20},
                {"x": 30, "y": 30},
                {"x": 20, "y": 40},
                {"x": 10, "y": 40},
                {"x": 00, "y": 30},
                {"x": 00, "y": 20},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
        }

        expected_result = {
            "type": "polygon",
            "points": [
                {"x": 10, "y": 10},
                {"x": 20, "y": 10},
                {"x": 30, "y": 20},
                {"x": 30, "y": 30},
                {"x": 20, "y": 40},
                {"x": 10, "y": 40},
                {"x": 00, "y": 30},
                {"x": 00, "y": 20},
            ],
            "id": "unicorn",
            "parents": [],
            "children": [],
            "area": 700.0,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_circle(self):
        json_object = {
            "type": "circle",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 10,
            "angleOfRotation": 0,
            "id": "unicorn",
        }

        expected_result = {
            "type": "circle",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 10,
            "angleOfRotation": 0,
            "id": "unicorn",
            "area": math.pi * 10 * 10,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_ellipse(self):
        json_object = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 0,
            "id": "unicorn",
        }

        expected_result = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 0,
            "id": "unicorn",
            "area": math.pi * 10 * 12,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_ellipse_rotated(self):
        json_object = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 30,
            "id": "unicorn",
        }

        expected_result = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 30,
            "id": "unicorn",
            "area": math.pi * 10 * 12,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_ellipse_overwrite(self):
        json_object = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 0,
            "id": "unicorn",
            "area": math.pi * 10 * 12,
        }

        expected_result = {
            "type": "ellipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 0,
            "id": "unicorn",
            "area": math.pi * 10 * 12,
        }

        add_area(json_object)

        self.assertDictEqual(json_object, expected_result)

    def test_value_error(self):
        json_object = {
            "type": "elipse",
            "center": {"x": 20, "y": 30},
            "radiusX": 10,
            "radiusY": 12,
            "angleOfRotation": 0,
            "id": "unicorn",
        }
        self.assertRaises(ValueError, add_area, json_object)
