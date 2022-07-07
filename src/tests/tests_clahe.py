import pytest

from PIL import Image, ImageFilter
from skimage.metrics import peak_signal_noise_ratio
from src.clahe.clahe import *
from src.preprocessing.preprocessing import *

# Create defined sample test images
img_name = "glioblastoma-84-coronal.jpg" #Choose the image you want to test on
processed_img= process_image(img_name) # Apply pre-processing filters
clahe_img =get_clahe_image(processed_img) # Apply the CLAHE algorithm on the prrocessed image
processed_hist= processed_img.histogram(processed_img)  # Calculate the histogram of the image after pre-processing only
clahe_hist = clahe_img.histogram(clahe_img) # Calculate the histogram of the image after pre-processing and CLAHE algorithm

def test_std_histogram():
        """
        Tests whether the clahe function is in fact implemented quantitatively,
        by comparing histogram standard deviation values.
        The improved image should have a higher standard deviation

        """
        #test this by printing the standard deviations
        #CLAHE algorithm should reduce the standart deviation of the histogram
        assert clahe_hist.stddev() > processed_hist.stddev()

def test_psnr():
        """
        Tests whether the clahe function is in fact implemented quantitatively,
        by comparing histogram peak signal to noise ratios.
        The improved image should have a lower psnr

        """
        #Checking PSNR ratio between the pre-processed image before and after applying CLAHE algorithem
        #Clahe should have higher PSNR
        psnr_clahe = peak_signal_noise_ratio(clahe_img, processed_img)
        assert psnr_clahe > 1