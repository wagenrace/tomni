import numpy as np

from numpy.testing import assert_array_equal
from unittest import TestCase

from .main import json2mask


class TestJson2Mask(TestCase):
    @classmethod
    def setUp(self):
        self.json_objects = [
            {
                "type": "polygon",
                "points": [
                    {"x": 2, "y": 2},
                    {"x": 2, "y": 4},
                    {"x": 4, "y": 4},
                    {"x": 4, "y": 2},
                ],
            }
        ]
        self.json_objects_small = [
            {
                "type": "polygon",
                "points": [
                    {"x": 2, "y": 2},
                    {"x": 4, "y": 2},
                ],
            }
        ]
        self.json_objects_tri = [
            {
                "type": "polygon",
                "points": [
                    {"x": 2, "y": 2},
                    {"x": 3, "y": 2},
                    {"x": 2, "y": 3},
                ],
            }
        ]
        self.json_objects_tri2 = [
            {
                "type": "polygon",
                "points": [
                    {"x": 2, "y": 2},
                    {"x": 5, "y": 5},
                    {"x": 8, "y": 2},
                ],
            }
        ]
        self.json_objects_multi = [
            {
                "type": "polygon",
                "points": [
                    {"x": 2, "y": 2},
                    {"x": 2, "y": 4},
                    {"x": 4, "y": 4},
                    {"x": 4, "y": 2},
                ],
            },
            {
                "type": "polygon",
                "points": [
                    {"x": 5, "y": 5},
                    {"x": 5, "y": 7},
                    {"x": 7, "y": 7},
                    {"x": 7, "y": 5},
                ],
            },
        ]
        self.img_dim = (10, 10)

    def test_single_object(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)
        expected_result[2:5, 2:5] = 1

        result = json2mask(self.json_objects, self.img_dim)

        assert_array_equal(expected_result, result)

    def test_single_tri(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)
        expected_result[2:4, 2] = 1
        expected_result[2, 2:4] = 1

        result = json2mask(self.json_objects_tri, self.img_dim)

        assert_array_equal(expected_result, result)

    def test_single_tri2(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)
        expected_result[2, 2:9] = 1
        expected_result[3, 3:8] = 1
        expected_result[4, 4:7] = 1
        expected_result[5, 5] = 1
        print(expected_result)

        result = json2mask(self.json_objects_tri2, self.img_dim)
        print(result)

        assert_array_equal(expected_result, result)

    def test_multiple_objects(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)
        expected_result[2:5, 2:5] = 1
        expected_result[5:8, 5:8] = 1

        result = json2mask(self.json_objects_multi, self.img_dim)

        assert_array_equal(expected_result, result)

    def test_to_small_objects(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)

        result = json2mask(self.json_objects_small, self.img_dim)

        assert_array_equal(expected_result, result)

    def test_to_small_objects_lim0(self):
        expected_result = np.zeros((10, 10), dtype=np.uint8)
        expected_result[2, 2:5] = 1

        result = json2mask(self.json_objects_small, self.img_dim, 0)

        assert_array_equal(expected_result, result)