import numpy as np


def grey_log_transformation(grey_img):
    """Returns the greyscale image after log transformation"""

    row, col = grey_img.shape
    transformed_img = np.zeros((row, col), dtype=np.uint8)

    c = round(255/np.log(np.max(grey_img)))
    for i in range(row):
        for j in range(col):
            transformed_img[i, j] = round(c * np.log(1 + grey_img[i, j]))

    return transformed_img


def color_log_transformation(b, g, r):
    """Returns the RGB image after log transformation"""

    row, col = b.shape
    transformed_img = np.zeros((row, col, 3), dtype=np.uint8)

    cb = round(255 / np.log(np.max(b)))
    cg = round(255 / np.log(np.max(g)))
    cr = round(255 / np.log(np.max(r)))

    for i in range(row):
        for j in range(col):
            transformed_img[i, j, 0] = round(cr * np.log(r[i, j]))
            transformed_img[i, j, 1] = round(cg * np.log(g[i, j]))
            transformed_img[i, j, 2] = round(cb * np.log(b[i, j]))

    return transformed_img
