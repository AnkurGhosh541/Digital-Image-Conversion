import numpy as np


def get_rgb_image(b, g, r):
    """Creates an RGB image from given Blue, Green and Red channels"""
    row, col = b.shape
    rgb_image = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rgb_image[i, j, 0] = r[i, j]
            rgb_image[i, j, 1] = g[i, j]
            rgb_image[i, j, 2] = b[i, j]

    return rgb_image
