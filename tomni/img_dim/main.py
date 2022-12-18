import numpy as np


# Chat API generated from unit test
# `can you write python code img_dim function so it passed these unit test:`
def img_dim(inArr, show_channel):
    if show_channel:
        return [inArr.shape[1], inArr.shape[0], inArr.shape[2]]
    else:
        return [inArr.shape[1], inArr.shape[0]]
