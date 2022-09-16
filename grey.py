import numpy as np


def grey_conversion(b, g, r):
    """Converts the RGB image to a Greyscale image from the given
     Red, Green and Blue Channel and returns the Greyscale image"""

    row, col = r.shape
    grey_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grey_chan[i, j] = r[i, j] * 0.30 + g[i, j] * 0.59 + b[i, j] * 0.11

    return grey_chan
