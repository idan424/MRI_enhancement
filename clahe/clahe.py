import numpy as np
from matplotlib import pyplot as plt 
import cv2

#clipLimit	- Threshold for contrast limiting.
#tileGridSize - Size of grid for histogram equalization. Input image will be divided into equally sized rectangular tiles. tileGridSize defines the number of tiles in row and column.

def get_clahe_image(processed_img, clipLimit=2.0, tileGridSize=(8,8)):
    clahe = cv2.createCLAHE(clipLimit , tileGridSize)
    cl_img = clahe.apply(processed_img)
    return cl_img
    
if __name__ == '__main__':
    img = ''
    print(get_clahe_image(processed_img))