import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from ui import get_img_names, plot_diff, user_params_selection
from preprocessing.preprocessing import process_image
from clahe.clahe import get_clahe_image


if __name__ == '__main__':
    clipLimit, tileGridSize = user_params_selection()
    img_names = get_img_names()

    for img_name in img_names:
        img = Image.open(img_name)
        pp_img = process_image(img)
        enc_img = get_clahe_image(pp_img, clipLimit, tileGridSize)

        plot_diff(np.array(img), pp_img, enc_img, img_name.split('/')[-1])

    plt.show()
