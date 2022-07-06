from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def get_img_names():
    '''
    This function asks from the user to choose files
    :return: a list of file names
    '''
    return list(filedialog.askopenfilenames(initialdir='images'))


def plot_diff(img, pp_img, enc, title, names=None):
    """
    This function shows the image before and after CLAHE
    :param img: the original image, np.ndarray
    :param enc: the enhanced image, np.ndarray
    """
    if names == None:
        names = ['Original image','Processed image','Enhanced image']
    fig, axs = plt.subplots(1,3)

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