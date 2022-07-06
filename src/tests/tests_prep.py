import pytest

from PIL import Image
from skimage.metrics import peak_signal_noise_ratio
from preprocessing import process_image


# Create defined sample test images
img_small = Image.new('RGB', (60, 30), color = 'red')
img_large = Image.new('RGB', (500, 300), color = 'red')
img_equal = Image.new('RGB', (256, 256), color = 'red')
img_gray  = img_equal.convert("L")
img_noisy = img_gray.effect_noise((256, 256), 200)  

# Calculate psnr (peak signal noise ration) metrics for greyscale resized image, verus image with added noise
psnr_noisy = peak_signal_noise_ratio(img_gray, img_noisy)

# Create an image with gaussian noise of size 256x256 and standard deviation 200

class TestPreprocessing:
    """
    A group of tests to evaluate sucessful preprocessing
    """
        
    def test_resize(self):
        """
        3 Tests for proper resizing of images: smaller, larger, and equal size images
        
        """
        processed_small = process_image(img_small)
        assert processed_small.size == (256, 256)
        processed_large = process_image(img_large)
        assert processed_large.size == (256, 256)
        processed_equal = process_image(img_equal)
        assert processed_equal.size == (256, 256)
        
    def test_greyscale(self):
        processed_gray = process_image(img_equal)
        assert processed_gray.mode() == img_gray.mode() 
        
        # alternative, requires import numpy
        # assert np.array(processed_gray).dtype() != np.uint8
    
    def test_denoised(self):
        processed_noisy = process_image(img_noisy)
        psnr_processed = peak_signal_noise_ratio(processed_noisy, img_noisy) 
        assert psnr_processed < psnr_noisy 
    
    
    
    
# if __name__ == "__main__":
#     # pytest.main()
#     unittest.main()
#     tests = TestPreprocessing()
#     methods = ["resize"]
#     errors = []

#     img_small = Image.new('RGB', (60, 30), color = 'red')
#     img_large = Image.new('RGB', (500, 300), color = 'red')
#     img_equal = Image.new('RGB', (256, 256), color = 'red')
#     img_grey  = img_equal.convert("L")
#     img_noisy = Image.effect_noise((256, 256), 200)    

    # for method in methods:
    #     try:
    #         getattr(tests, "test_" + method)()
    #     except AssertionError as e:
    #         errors.append(f"Failed when testing method 'test_{method}': {e}")

    # if len(errors) > 0:
    #     print(errors)
    # else:
    #     print("Tests pass successfully.")
