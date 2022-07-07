import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import tkinter as tk
from tkinter import filedialog

from src.preprocessing.preprocessing import process_image
from src.clahe.clahe import get_clahe_image

root = tk.Tk()


def get_img_names():
    """
    This function asks from the user to choose files
    :return: a list of file names
    """
    return list(filedialog.askopenfilenames(initialdir='images'))


class GUI:
    """
    This class let's a user to use the program via a graphical user interface
    """
    default_cl = 2.0
    default_gs = (8, 8)

    def __init__(self):
        """
        This function constructs the gui and it's functionality
        """
        self.cl = 2.0
        self.gs = 8

        self.root = root

        # Contrast Limit input
        self.cl_label = tk.Label(text="Choose Threshold for contrast limiting\n" +
                                      "(Default = 2.0)")
        self.cl_label.pack()

        self.cl_entry = tk.Entry()
        self.cl_entry.pack()

        # Grid Size input
        self.gs_label = tk.Label(text="Grid size for histogram equalization.\n" +
                                      "Choose a single integer. (Default = 8)")
        self.gs_label.pack()

        self.gs_entry = tk.Entry()
        self.gs_entry.pack()

        # Choose images to process
        self.im_button = tk.Button(text="Choose images to process",
                                   command=self.button_press)
        self.im_button.pack()

        self.root.mainloop()
        # self.root.withdraw()

    def button_press(self):
        """
        This function is taking care of a button press
        """

        # Update the Clip Limit
        if self.cl_entry.get():
            try:
                self.cl = float(self.cl_entry.get())

            except Exception as e:
                print(e)
                raise e
        else:
            self.cl = self.default_cl

        # Update the Grid Size
        if self.gs_entry.get():
            try:
                gs = int(self.gs_entry.get())
                self.gs = (gs, gs)
            except Exception as e:
                print(e)
                raise e
        else:
            self.gs = self.default_gs

        print(f'ClipLimit={self.cl}, GridSize={self.gs}')

        # use the set clip limit and grid size to process images
        self.process_images()

    def process_images(self):
        """
        This function gets all image names and process them
        :return:
        """
        img_names = get_img_names()

        for img_name in img_names:
            # run over all choosen images, aplly the pre-rocessing and the CLAHE algorithem

            img = np.array(Image.open(img_name))
            pp_img = process_image(img_name)
            enc_img = get_clahe_image(pp_img, self.cl, self.gs)

            # show the results of the 3 processing stats of the image - Originale,after pre-processing,after CLAHE algorithem
            plot_diff(img, pp_img, enc_img, img_name.split('/')[-1])

        plt.show()


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
    GUI()
