#Requirements: pip install Pillow
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageOps, ImageFilter, ImageStat
from skimage import data, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage.metrics import peak_signal_noise_ratio
from skimage.util import random_noise


def process_image(img_path_name):
    """
    :param img_path_name: Input image path string
    :return: preprocessed image, np.array of size (256,256)
    
    """
    img = Image.open(img_path_name)
    
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    
    image_resz_gray = ImageOps.grayscale(img_resized) #pixel value range = (0,254)
    
    #Denoising with non-local means
    stats = ImageStat.Stat(image_resz_gray)
    float_img = float(image_resz_gray)
    
    print(stats.stddev)
    
    
    processed_img = image_resz_gray #temporary, until I finish denoising
    return processed_img
    
if __name__ == '__main__':
    img_path_name = "../images/glioblastoma-84-coronal.jpg"
    pp_img = process_image(img_path_name)
    

#image.save('image_resz_gray.jpg')
#Testing things:
# print(image.format)
# print(image.size)
# print(image.mode)

# print(image_resz_gray.format)
# print(image_resz_gray.size)
# print(image_resz_gray.mode)
# # show the image
# image.show()
# image_resz_gray.show()

#Size of the image in pixels
#width, height = image.size