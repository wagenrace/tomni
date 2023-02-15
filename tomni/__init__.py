# -*- coding: utf-8 -*-
"""Tomni is a collection of image analysis functions useful for CytoSmart solution."""

__author__ = """Tom Nijhof & Jelle van Kerkvoorde"""
__email__ = "tom.nijhof@cytosmart.com"
__version__ = "2.0.0b0"

from .annotation_manager import AnnotationManager
from .annotation_manager.annotations import Ellipse
from .annotation_manager.annotations import Point
from .annotation_manager.annotations import Polygon
from .bbox_fitting import bbox_fitting, bbox_fitting_center
from .bbox_operations import check_overlap_bbox
from .convert_color import convert_color
from .illumination_correction import (
    absolute_difference,
    fluo_tophat,
    relative_difference,
)
from .img_dim import img_dim
from .img_paste import img_paste
from .json_operations import *
from .make_mask import *
from .shape_fitting import fit_rect_around_ellipse
from .transformers import *
