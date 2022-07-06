#Requirements: pip install Pillow
from PIL import Image, ImageOps, ImageFilter



def process_image(img_path_name):
    img = Image.open(img_path_name)
    newsize = (256, 256)
    img_resized = img.resize(newsize)
    image_resz_gray = ImageOps.grayscale(img_resized)
    
    processed_img = image_resz_gray #temporary, until I finish denoising
    return processed_img
    
if __name__ == '__main__':
    img_path_name = "images/glioblastoma-84-coronal.jpg"
    process_image(img_path_name)
    

#image.save('image_resz_gray.jpg')
#Testing things:
# print(image.format)
# print(image.size)
# print(image.mode)

# print(image_resz_gray.format)
# print(image_resz_gray.size)
# print(image_resz_gray.mode)
# # show the image
# image.show()
# image_resz_gray.show()

# Size of the image in pixels
#width, height = image.size