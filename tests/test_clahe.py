import pytest
import numpy as np

from PIL import Image, ImageFilter
from skimage.metrics import peak_signal_noise_ratio
from src.clahe.clahe import get_clahe_image
from src.preprocessing.preprocessing import process_image

# Create defined sample test images
img_name = "images/glioblastoma-84-coronal.jpg" # Choose the image you want to

# Apply pre-processing filters
pp_img = process_image(img_name)
# Apply the CLAHE algorithm on the prrocessed image
clahe_img = get_clahe_image(pp_img)

def test_std_histogram():
    """
    Tests whether the clahe function is in fact implemented quantitatively,
    by comparing histogram standard deviation values.
    CLAHE algorithm should reduce the standard deviation of the histogram
    Therefore, the improved image should have a higher standard deviation
    """

    # Calculate the histogram of the image after pre-processing only
    pp_hist, _ = np.histogram(pp_img)
    # Calculate the histogram of the image after pre-processing and CLAHE algorithm
    clahe_hist, _ = np.histogram(clahe_img)

    assert clahe_hist.std() < pp_hist.std()

def test_psnr():
    """
    Tests whether the clahe function is in fact implemented quantitatively,
    by comparing histogram peak signal-to-noise ratios.
    The improved image should have a lower psnr
    Checking PSNR ratio between the pre-processed image before and after applying
    CLAHE algorithem
    """

    # Clahe should have higher PSNR
    psnr_clahe = peak_signal_noise_ratio(clahe_img.astype(np.int8), pp_img.astype(np.int8))
    print("psnr clahe: ", + psnr_clahe)
    assert psnr_clahe > 1