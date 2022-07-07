import pytest

from PIL import Image, ImageFilter
from skimage.metrics import peak_signal_noise_ratio
from clahe import get_clahe_image

# Create defined sample test images
img_equal = Image.new('RGB', (256, 256), color = 'red')
img_gray  = img_equal.convert("L")
img_noisy = img_gray.effect_noise((256, 256), 200)  
img_blurred = img_noisy.filter(ImageFilter.BLUR)

class TestCLAHE:
    """
    A group of tests to evaluate sucessful clahe implementation
    by comparing histogram mean value, standard deviation, and psnr values 
    
    """
    
    clahe_img = get_clahe_image(img_noisy)
    clahe_hist = clahe_img.histogram()
    blurred_hist= img_blurred.histogram()   
    
    # Calculate psnr (peak signal noise ratio) metrics for greyscale resized image, verus image with added noise
    psnr_noisy = peak_signal_noise_ratio(img_gray, img_noisy) 
    
    def test_mean_histogram(self):
        """
        Tests whether the clahe function is in fact implemented quantitatively, 
        by comparing mean histogram values
        
        """
        #test this by viewing the histograms, and printing the means
        #decide if it should be > or <, not !=
        assert self.clahe_hist.mean() != self.blurred_hist.mean()
        
    def test_std_histogram(self):
        """
        Tests whether the clahe function is in fact implemented quantitatively, 
        by comparing histogram standard deviation values. 
        The improved image should have a higher standard deviation
        
        """
        #test this by printing the standard deviations
        assert self.clahe_hist.stddev() > self.blurred_hist.stddev()

    def test_psnr(self):
        """
        Tests whether the clahe function is in fact implemented quantitatively, 
        by comparing histogram peak signal to noise ratios. 
        The improved image should have a lower psnr
        
        """
        #test this by printing the psnr
        psnr_clahe = peak_signal_noise_ratio(self.clahe_img, img_noisy) 
        assert psnr_clahe < self.psnr_noisy 