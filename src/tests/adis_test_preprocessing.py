from src.preprocessing.preprocessing import *
from ui import get_img_names, plot_diff, user_params_selection
from PIL import Image

import pandas as pd
import numpy as np
import pytest

img_name = "glioblastoma-84-coronal.jpg" #Choose the image you want to test on
img_gray  = Image.new('RGB', (256, 256), color = 'red').convert("L") # Create gray same size image in order to check the final image mode
img_small = [] # import path to the smaller size image
img_large = [] # import path to the larger size image

 
def test_original_image_resize():
    """
    Test for proper resizing of image from the Database: img_name
        
    """
    Processed_image = process_image(img_name)
    assert Processed_image.size == (256, 256)

def test_resize():
    """
   2 Tests for proper resizing of images: smaller, larger than final size
        
    """

    processed_small = process_image(img_small)
    assert processed_small.size == (256, 256)
    processed_large = process_image(img_large)
    assert processed_large.size == (256, 256)

        
def test_greyscale():
        processed_gray = process_image(img_name)
        assert processed_gray.mode() == img_gray.mode() 
        
        
def test_denoised(self):
    """
        Tests whether the preprocessing sucessfully redoces noise
        by comparing histogram peak signal to noise ratios.
        The improved image should have a lower psnr

    """
    img = Image.open(img_path)
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    pre_processed_img = np.array(ImageOps.grayscale(img_resized)).astype(float)
    processed_img = process_image(img_name)
    psnr_processed = peak_signal_noise_ratio(processed_img, img_noisy) 
    assert psnr_processed < psnr_noisy 
    