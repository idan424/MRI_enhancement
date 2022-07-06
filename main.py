import matplotlib.image as mpimg

from preprocessing.preprocessing import process_image
from clahe.clahe import process_and_show


if __name__ == '__main__':
    img = mpimg.imread('images/glioblastoma-84-coronal.jpg').mean(axis=2)
    enc = process_and_show(img)
