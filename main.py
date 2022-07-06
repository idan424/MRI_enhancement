import matplotlib.image as mpimg

from preprocessing.preprocessing import process_image
from clahe.clahe import enhance_and_show, plot_diff


if __name__ == '__main__':
    img_name = 'images/glioblastoma-84-coronal.jpg'
    img = mpimg.imread(img_name).mean(axis=2)

    pp_img = process_image(img_name)
    plot_diff(img, pp_img, names=['original image', 'preprocessed image'])

    enc = enhance_and_show(pp_img)
