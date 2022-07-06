import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from ui import get_img_names, plot_diff
from preprocessing.preprocessing import process_image
from clahe.clahe import get_clahe_image


if __name__ == '__main__':
    #In order to run on our module if it is the source file
    img_names = get_img_names()

    for img_name in img_names:
        #run over all choosen images, aplly the pre-rocessing and the CLAHE algorithem 
        
        img = np.array(Image.open(img_name))
        pp_img = process_image(img_name)
        enc_img = get_clahe_image(pp_img)

        # show the results of the 3 processing stats of the image - Originale,after pre-processing,after CLAHE algorithem
        plot_diff(img, pp_img, enc_img, img_name.split('/')[-1])

    plt.show()

