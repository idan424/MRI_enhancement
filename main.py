import matplotlib.image as mpimg

from preprocessing.preprocessing import process_image
from clahe.clahe import enhance_and_show, plot_diff


if __name__ == '__main__':
    img = mpimg.imread('images/glioblastoma-84-coronal.jpg').mean(axis=2)

    pp_img = process_image(img)
    plot_diff(img, pp_img)

    enc = enhance_and_show(pp_img)
