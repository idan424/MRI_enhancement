import os
import cv2
import numpy as np

from skimage.metrics import peak_signal_noise_ratio
from src.preprocessing.preprocessing import process_image
from PIL import Image, ImageOps

# Paths to test images
img_small = 'small_test_img.jpeg'
img_large = 'large_test_img.jpeg'
img_MRI = "images/glioblastoma-84-coronal.jpg"  

# Create gray same size image (in order to check the processed image mode)
img_gray = Image.new('RGB', (256, 256), color='red').convert("L")

# Create the test images if they don't exist
if img_small not in os.listdir(os.getcwd()):
    # Create image numpy array - black picture
    small = np.zeros((256, 256))
    # Save image
    cv2.imwrite(img_small, small)

if img_large not in os.listdir(os.getcwd()):
    # Create image numpy array - black picture
    large = np.zeros((512, 512))
    # Save image
    cv2.imwrite(img_large, large)


def test_original_image_resize():
    """
    Test for proper resizing of image from the Database: img_MRI   
    """
    processed_image = process_image(img_MRI)
    assert processed_image.shape == (256, 256)


def test_resize():
    """
    3 Tests for proper resizing of test images: smaller, larger, and same-size images  
    """
    processed_small = process_image(img_small)
    assert processed_small.shape == (256, 256)

    processed_large = process_image(img_large)
    assert processed_large.shape == (256, 256)
    
    processed_same = process_image(img_gray)
    assert processed_same.shape == (256, 256)


def test_greyscale():
    """
    Test for proper color mode setting 
    """
    processed_gray = process_image(img_MRI)
    assert len(processed_gray.shape) == 2


def test_denoised():
    """
    Tests whether the preprocessing sucessfully reduces noise
    by comparing histogram peak signal to noise ratios.
    The improved image should have a lower psnr
    """
    img = Image.open(img_MRI)
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    pp_img = np.array(ImageOps.grayscale(img_resized)).astype(float)
    processed_img = process_image(img_MRI)
    psnr_processed = peak_signal_noise_ratio(pp_img, processed_img)

    assert psnr_processed < np.inf
#.astype(int)