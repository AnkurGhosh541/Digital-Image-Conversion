import numpy as np


def negative_grey_conversion(grey_img):
    """Converts the Greyscale image to a Negative image returns the Negative image"""

    row, col = grey_img.shape
    negative_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_chan[i, j] = abs(grey_img[i, j] - 255)

    return negative_chan


def negative_color_conversion(b, g, r):
    """Converts the BGR image to a Negative image from the given
         Blue, Green and Red Channel and returns the Negative image"""

    row, col = b.shape
    negative_chan = np.zeros((row, col, channel), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_chan[i, j, 0] = abs(r[i, j] - 255)
            negative_chan[i, j, 1] = abs(g[i, j] - 255)
            negative_chan[i, j, 2] = abs(b[i, j] - 255)

    return negative_chan
