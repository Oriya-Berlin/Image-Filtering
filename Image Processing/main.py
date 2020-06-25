from CleanNoises import *
from ColorFiltering import *
from Brightness import *
from Contrasts import *


if __name__ == "__main__":

    '''
    img_1 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
    img_1.show()
    bright_image = set_brightness(img_1, 60)
    bright_image.show()
    '''

    '''
    img_2 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/cat.bmp')
    img_2 = img_2.convert('RGB')
    img_2.show()
    clean_img = clean_sp(img_2)
    clean_img.show()
    '''

    '''
    img_3 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
    img_3.show()
    filtered_image = color_filtering(img_3, 'green')
    filtered_image.show()
    '''

    '''
    img_4 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
    img_4.show()
    # the first formula
    contrast_image_1 = set_contrast_1(img_4, 210)
    contrast_image_1.show()
    # the second formula
    contrast_image_2 = set_contrast_2(img_4, -20)
    contrast_image_2.show()
    '''

    '''
    img_5 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
    img_5.show()
    inverted_image = set_invert(img_5)
    inverted_image.show()
    '''

    '''
    img_6 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/dark.jpeg')
    img_6.show()
    corrected_image = set_gamma_correction(img_6, 5)
    corrected_image.show()
    '''



