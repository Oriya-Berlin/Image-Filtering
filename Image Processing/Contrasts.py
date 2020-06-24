import numpy as np
from PIL import Image



contrasts = ()


#
def contrast_formula_1(contrast_value, RGB_component):
    factor = float((259*(contrast_value+255))/(255*(259-contrast_value)))
    new_value = factor*(RGB_component-128) + 128

    if new_value > 255:
        new_value = 255
    if new_value < 0:
        new_value = 0

    return new_value

# -------------------------------------------------------------


#
def get_brightness_value(matrix, height, width):  # 'b' value on the formula
    b_red, b_green, b_blue = 0, 0, 0

    for i in range(0, height):
        for j in range(0, width):

            b_red += matrix[i][j][0]
            b_green += matrix[i][j][1]
            b_blue += matrix[i][j][2]

    b_red = float(b_red/(height*width))
    b_green = float(b_green/(height*width))
    b_blue = float(b_blue/(height*width))
    brightness_vector = [b_red, b_green, b_blue]
    return brightness_vector


#
def contrast_formula_2(contrast_value, brightness_value, RGB_component):
    new_value = (contrast_value * (RGB_component - brightness_value)) + brightness_value

    if new_value > 255:
        new_value = 255
    if new_value < 0:
        new_value = 0

    return new_value

# -------------------------------------------------------------


#
def set_contrast(img, contrast_value, contrast_method='default_contrast'):
    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    #if contrast_method not in contrasts:
    #   raise Exception('')

    for i in range(0, height):
        for j in range(0, width):
            R = matrix[i][j][0]
            R = default_contrast(contrast_value, R)
            G = matrix[i][j][1]
            G = default_contrast(contrast_value, G)
            B = matrix[i][j][2]
            B = default_contrast(contrast_value, B)

            matrix[i][j] = [R, G, B]

    matrix = Image.fromarray(np.uint8(matrix))
    return matrix


my_img = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
my_img.show()
contrast_image = set_contrast(my_img, -500)
contrast_image.show()









