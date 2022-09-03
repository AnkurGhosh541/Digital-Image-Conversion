import cv2
import numpy as np


def get_color_channels(img):
    """Returns the red, green and blue channels in a list format"""

    row, col, channel = img.shape
    r_chan = np.zeros((row, col), dtype=np.uint8)
    g_chan = np.zeros((row, col), dtype=np.uint8)
    b_chan = np.zeros((row, col), dtype=np.uint8)

    for i, row in enumerate(img):
        for j, col in enumerate(row):
            b, g, r = col

            r_chan[i, j] = r
            g_chan[i, j] = g
            b_chan[i, j] = b

    return [r_chan, g_chan, b_chan]


def grey_conversion(r, g, b):
    """Converts the RGB image to a Greyscale image from the given
     Red, Green and Blue Channel and returns the Greyscale image"""

    row, col = r.shape
    grey_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grey_chan[i, j] = r[i, j] * 0.30 + g[i, j] * 0.59 + b[i, j] * 0.11

    return grey_chan


def negative_grey_conversion(grey_img):
    """Converts the Greyscale image to a Negative image returns the Negative image"""

    row, col = grey_img.shape
    negative_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_chan[i, j] = abs(grey_img[i, j] - 255)

    return negative_chan


def negative_color_conversion(r, g, b, img):
    """Converts the RGB image to a Negative image from the given
         Red, Green and Blue Channel and returns the Negative image"""

    row, col, channel = img.shape
    negative_chan = np.zeros((row, col, channel), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_chan[i, j, 0] = abs(r[i, j] - 255)
            negative_chan[i, j, 1] = abs(g[i, j] - 255)
            negative_chan[i, j, 2] = abs(b[i, j] - 255)

    return negative_chan


def rotate_image(grey_img):
    """Rotates the given Greyscale image anticlockwise"""

    row, col = grey_img.shape
    rotated_img = np.zeros((col, row), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rotated_img[j, i] = grey_img[i, j]

    return rotated_img


if __name__ == '__main__':
    image = cv2.imread("PATH/TO/IMAGE")

    rChan, gChan, bChan = get_color_channels(image)

    grey_image = grey_conversion(rChan, gChan, bChan)
    negative_grey_image = negative_grey_conversion(grey_image)
    negative_color_image = negative_color_conversion(rChan, gChan, bChan, image)
    rotated_image = rotate_image(grey_image)

    nrChan, ngChan, nbChan = get_color_channels(negative_color_image)
    new_negative_img = negative_color_conversion(nrChan, ngChan, nbChan, negative_color_image)

    cv2.imshow("Grey Image", grey_image)
    cv2.imshow("Negative Grey Image", negative_grey_image)
    cv2.imshow("Negative Color Image", negative_color_image)
    cv2.imshow("Normal image", new_negative_img)
    cv2.imshow("Rotated Grey Image", rotated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
