from src.clahe.clahe import get_clahe_image
from PIL import Image, ImageFilter

# Create defined sample test images
img_equal = Image.new('RGB', (256, 256), color = 'red')
img_gray  = img_equal.convert("L")
img_noisy = img_gray.effect_noise((256, 256), 200)  
img_blurred = img_noisy.filter(ImageFilter.BLUR)

class TestPreprocessing:
    """
    A group of tests to evaluate sucessful clahe implementation
    """
        
    def test_mean_histogram(self):
        """
        Tests whether the clahe function is in fact implemented quantitatively,
        by comparing mean histogram values
        
        """
    
        clahe_img = get_clahe_image(img_noisy)
        clahe_hist = clahe_img.histogram()
        blurred_hist= img_blurred.histogram()
        #test this by viewing the histograms, and printing the means
        #decide if it should be > or <, not !=
        assert clahe_hist.mean() != blurred_hist.mean()
    
    # Create a test for different parameter values