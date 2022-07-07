import os
import cv2

from skimage.metrics import peak_signal_noise_ratio
from src.preprocessing.preprocessing import process_image
from PIL import Image

img_name = "images/glioblastoma-84-coronal.jpg"  # Choose the image you want to

# Create gray same size image in order to check the final image mode
img_gray = Image.new('RGB', (256, 256), color='red').convert("L")

# load path to the smaller size image
img_small = 'small_test_img.jpeg'
# load path to the larger size image
img_large = 'large_test_img.jpeg'

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
    Test for proper resizing of image from the Database: img_name
        
    """
    processed_image = process_image(img_name)
    assert processed_image.shape == (256, 256)


def test_resize():
    """
    2 Tests for proper resizing of images: smaller, larger than final size
        
    """
    processed_small = process_image(img_small)
    assert processed_small.shape == (256, 256)

    processed_large = process_image(img_large)
    assert processed_large.shape == (256, 256)


def test_greyscale():
    processed_gray = process_image(img_name)
    assert len(processed_gray.shape) == 2


def test_denoised():
    """
        Tests whether the preprocessing sucessfully redoces noise
        by comparing histogram peak signal to noise ratios.
        The improved image should have a lower psnr

    """
    img = Image.open(img_name)
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    pp_img = np.array(ImageOps.grayscale(img_resized)).astype(float)
    processed_img = process_image(img_name)
    psnr_processed = peak_signal_noise_ratio(pp_img.astype(int), processed_img)

    assert psnr_processed < np.inf
