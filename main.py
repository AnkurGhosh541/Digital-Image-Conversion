import cv2
import matplotlib.pyplot as plt

from channels import get_color_channels
from grey import grey_conversion
from rgb import get_rgb_image
from rotate import *
from negative import *
from log_transformation import *
from ycbcr import *


if __name__ == '__main__':
    image = cv2.imread("/PATH/TO/IMAGE")
    b, g, r = get_color_channels(image)
    grey_image = grey_conversion(b, g, r)

    fig = plt.figure(figsize=(16, 10))
    plt_x = 3
    plt_y = 3

    fig.add_subplot(plt_x, plt_y, 1)
    plt.imshow(get_rgb_image(b, g, r))
    plt.axis("off")
    plt.title("Original image")

    fig.add_subplot(plt_x, plt_y, 2)
    plt.imshow(grey_image, cmap="gray")
    plt.axis("off")
    plt.title("Greyscale image")

    fig.add_subplot(plt_x, plt_y, 3)
    plt.imshow(rotate_clockwise_grey(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Rotated clockwise grey")

    fig.add_subplot(plt_x, plt_y, 4)
    plt.imshow(rotate_anticlockwise_grey(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Rotated anticlockwise grey")

    fig.add_subplot(plt_x, plt_y, 5)
    plt.imshow(mirror_horizontal_grey(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Mirrored horizontal grey")

    fig.add_subplot(plt_x, plt_y, 6)
    plt.imshow(mirror_vertical_grey(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Mirrored vertical grey")

    fig.add_subplot(plt_x, plt_y, 7)
    plt.imshow(negative_grey_conversion(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Negative greyscale image")

    fig.add_subplot(plt_x, plt_y, 8)
    plt.imshow(grey_log_transformation(grey_image), cmap="gray")
    plt.axis("off")
    plt.title("Log transformed grey image")

    fig.add_subplot(plt_x, plt_y, 9)
    plt.imshow(rgb_to_ycbcr(b, g, r))
    plt.axis("off")
    plt.title("YCbCr image")

    plt.show()
