from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


def get_img_names():
    """
    This function asks from the user to choose files
    :return: a list of file names
    """
    return list(filedialog.askopenfilenames(initialdir='images'))


def user_params_selection():
    """
    This function asks the user to define that algorithm parameters

    :return: float, tuple(int,int) : answers of the user
    """

    choose = input('Do you want to choose params?(Y/N)')
    if choose.lower() == 'y':
        try:
            clipLimit = input("Choose Threshold for contrast limiting (Default = 2.0): ")
            clipLimit = float(clipLimit)
            n = input("Size of grid for histogram equalization." +
                      "Defines the number of tiles in row and column (Default = (8,8)): ")
            tileGridSize = (int(n), int(n))
        except Exception as e:
            print(e)
            raise e
    else:
        print('using default values')
        clipLimit = 2.0
        tileGridSize = (8, 8)

    return clipLimit, tileGridSize


def plot_diff(img, pp_img, enc, title, names=None):
    """
    This function shows the image before and after CLAHE
    :param img: the original image, np.ndarray
    :param enc: the enhanced image, np.ndarray
    """
    if names == None:
        names = ['Original image', 'Processed image', 'Enhanced image']

    fig, axs = plt.subplots(1, 3)
    axs[0].imshow(img, cmap='gray')

    axs[0].set_title(names[0])
    axs[1].imshow(pp_img, cmap='gray')

    axs[1].set_title(names[1])
    axs[2].imshow(enc, cmap='gray')

    axs[2].set_title(names[2])
    for ax in axs:
        ax.set_xticks([])
        ax.set_yticks([])

    plt.suptitle(title)


if __name__ == '__main__':
    imgs = get_img_names()
