import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from ui import get_img_names, plot_diff
from preprocessing.preprocessing import process_image
from clahe.clahe import get_clahe_image


if __name__ == '__main__':
    img_names = get_img_names()

    for img_name in img_names:
        img = np.array(Image.open(img_name))
        pp_img = process_image(img_name)
        enc_img = get_clahe_image(pp_img)

        plot_diff(img, pp_img, enc_img, img_name.split('/')[-1])

    plt.show()

