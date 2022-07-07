import numpy as np

from PIL import Image, ImageOps
from skimage.restoration import denoise_nl_means, estimate_sigma


def process_image(img_path):
    """
    This function pre-processes an image by
    -resizing to 256x256
    -converting to grayscale
    -performing noise reduction algorithm of non-local means
    :param img_path_name: Input image path string
    :return: preprocessed image, np.ndarray of size (256,256)
    """
        # Non-Local means parameter explanations:
        # larger h =  smoothing between disimilar patches
        # fast_mode = false adds spatial gaussian gradient

    img = Image.open(img_path)
    
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    np_img = np.array(ImageOps.grayscale(img_resized)).astype(float)

    # Denoising with non-local means
    sigma_est = np.mean(estimate_sigma(np_img))      # estimate the noise standard deviation from the noisy image
    patch_kw = dict(patch_size=5, patch_distance=6)  # 5x5 patches, 13x13 search area
    processed_img = denoise_nl_means(np_img, h=1.15 * sigma_est, sigma=sigma_est, fast_mode=True, **patch_kw)

    return processed_img

if __name__ == '__main__':
    img_path= "images/glioblastoma-84-coronal.jpg"
    pp_img = process_image(img_path)