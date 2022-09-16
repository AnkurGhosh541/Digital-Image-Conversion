import numpy as np


def rgb_to_ycbcr(b, g, r):
    """Creates a YCbCr image from Blue, Green and Red Channels"""

    row, col = b.shape
    ycbcr = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            ycbcr[i, j, 0] = round(0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j])
            ycbcr[i, j, 1] = round(0.500 * r[i, j] - 0.418688 * g[i, j] - 0.081312 * b[i, j])
            ycbcr[i, j, 2] = round(-0.168736 * r[i, j] - 0.331264 * g[i, j] + 0.500 * b[i, j])

    return ycbcr


def ycbcr_to_rgb(y, cb, cr):
    """Creates an RGB image from Y, Cb and Cr Channels"""

    row, col = y.shape
    rgb = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rgb[i, j, 0] = round(1 * y[i, j] + 0.0 * cb[i, j] + 1.402 * cr[i, j])
            rgb[i, j, 1] = round(1 * y[i, j] - 0.344136 * cb[i, j] - 0.714136 * cr[i, j])
            rgb[i, j, 2] = round(1 * y[i, j] + 1.772 * cb[i, j] + 0 * cr[i, j])

    return rgb
