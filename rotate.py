import numpy as np


def mirror_horizontal_grey(grey_img):
    """Mirrors a greyscale image horizontally"""

    row, col = grey_img.shape
    rotated_img = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[i, j] = grey_img[i, col - 1 - j]

    return rotated_img


def mirror_horizontal_color(b, g, r):
    """Mirrors an RGB image horizontally"""

    row, col = b.shape
    rotated_img = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[i, j, 0] = r[i, col - 1 - j]
            rotated_img[i, j, 1] = g[i, col - 1 - j]
            rotated_img[i, j, 2] = b[i, col - 1 - j]

    return rotated_img


def mirror_vertical_grey(grey_img):
    """Mirrors a greyscale image vertically"""

    row, col = grey_img.shape
    rotated_img = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[i, j] = grey_img[row - 1 - i, j]

    return rotated_img


def mirror_vertical_color(b, g, r):
    """Mirrors an RGB image vertically"""

    row, col = b.shape
    rotated_img = np.zeros((row, col, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[i, j, 0] = r[row - 1 - i, j]
            rotated_img[i, j, 1] = g[row - 1 - i, j]
            rotated_img[i, j, 2] = b[row - 1 - i, j]

    return rotated_img


def rotate_clockwise_grey(grey_img):
    """Rotates a greyscale image clockwise"""

    row, col = grey_img.shape
    rotated_img = np.zeros((col, row), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[j, row - 1 - i] = grey_img[i, j]

    return rotated_img


def rotate_clockwise_color(b, g, r):
    """Rotates an RGB image clockwise"""

    row, col = b.shape
    rotated_img = np.zeros((col, row, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[j, row - 1 - i, 0] = r[i, j]
            rotated_img[j, row - 1 - i, 1] = g[i, j]
            rotated_img[j, row - 1 - i, 2] = b[i, j]

    return rotated_img


def rotate_anticlockwise_grey(grey_img):
    """Rotates a greyscale image clockwise"""

    row, col = grey_img.shape
    rotated_img = np.zeros((col, row), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[col - 1 - j, i] = grey_img[i, j]

    return rotated_img


def rotate_anticlockwise_color(b, g, r):
    """Rotates an RGB image clockwise"""

    row, col = b.shape
    rotated_img = np.zeros((col, row, 3), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[col - 1 - j, i, 0] = r[i, j]
            rotated_img[col - 1 - j, i, 1] = g[i, j]
            rotated_img[col - 1 - j, i, 2] = b[i, j]

    return rotated_img
