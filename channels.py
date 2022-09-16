import numpy as np


def get_color_channels(img):
    """Returns the red, green and blue channels in a list format"""

    row, col, channel = img.shape
    chan1 = np.zeros((row, col), dtype=np.uint8)
    chan2 = np.zeros((row, col), dtype=np.uint8)
    chan3 = np.zeros((row, col), dtype=np.uint8)

    for i, row in enumerate(img):
        for j, col in enumerate(row):
            b, g, r = col

            chan1[i, j] = r
            chan2[i, j] = g
            chan3[i, j] = b

    return chan1, chan2, chan3
