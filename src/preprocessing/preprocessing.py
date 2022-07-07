import numpy as np

from PIL import Image, ImageOps
from skimage.restoration import denoise_nl_means, estimate_sigma


def process_image(img_path: str):
    """
    This function pre-processes an image by
        -resizing to 256x256
        -converting to grayscale
        -performing noise reduction algorithm of non-local means

    Non-Local means parameter explanations:
        larger h =  smoothing between dissimilar patches
        fast_mode = false adds spatial gaussian gradient

    :param img_path: path to the image
    :return: preprocessed image, np.ndarray of size (256,256)
    """

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
    # For testing one file
    import pathlib
    img_path = (pathlib.Path(__file__).parent / '../../images/glioblastoma-84-coronal.jpg').resolve()
    pp_img = process_image(img_path)
    