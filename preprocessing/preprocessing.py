#Requirements: pip install Pillow
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageOps, ImageMath, ImageStat
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
    
    ##Denoising with non-local means
    np_img = np.array(image_resz_gray).astype(float)

    # estimate the noise standard deviation from the noisy image
    sigma_est = np.mean(estimate_sigma(np_img))
    patch_kw = dict(patch_size=5, patch_distance=6)
    processed_img = denoise_nl_means(np_img, h=0.6 * sigma_est, sigma=sigma_est,
                                     fast_mode=True, **patch_kw)

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