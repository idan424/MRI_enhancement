import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

import cv2


def get_clahe_image(img: np.ndarray, clipLimit=2.0, tileGridSize=(8, 8)):
    """

    :param img: Input image, np.array of size (256,256)
    :param clipLimit: Threshold for contrast limiting.
    :param tileGridSize: Size of grid for histogram equalization.
                         Input image will be divided into equally sized
                         rectangular tiles. tileGridSize defines the number
                         of tiles in row and column.
    :return: clahe image, np.array of size (256,256)
    """
    gray_image = img.astype(np.uint8) if img.dtype != np.uint8  else img

    clahe = cv2.createCLAHE(clipLimit, tileGridSize)
    cl_img = clahe.apply(gray_image)

    return cl_img


if __name__ == '__main__':
    img = mpimg.imread('../images/glioblastoma-84-coronal.jpg').mean(axis=2)
    enc = get_clahe_image(img)
    plt.imshow(enc)
