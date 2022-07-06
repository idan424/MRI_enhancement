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


def plot_diff(img, enc):
    """
    This function shows the image befor and after CLAHE
    :param img: the original image, np.ndarray
    :param enc: the enhanced image, np.ndarray
    """

    fig, axs = plt.subplots(1,2)

    axs[0].imshow(img, cmap='gray')
    axs[0].set_title('Original image')

    axs[1].imshow(enc, cmap='gray')
    axs[1].set_title('Enhanced image')
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

def process_and_show(img):
    """

    :param img: The image to process and present the, np.ndarray
    :return: clahe output image, np.ndarray
    """

    enc = get_clahe_image(img)
    plot_diff(img, enc)

    return enc


if __name__ == '__main__':
    img = mpimg.imread('../images/glioblastoma-84-coronal.jpg').mean(axis=2)
    enc = process_and_show(img)

