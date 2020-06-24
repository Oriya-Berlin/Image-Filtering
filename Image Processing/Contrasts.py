import numpy as np
from PIL import Image


# -------------------------------------------------------------
#
def contrast_formula_1(contrast_value, RGB_component):
    factor = float((259*(contrast_value+255))/(255*(259-contrast_value)))
    new_value = (factor*(RGB_component-128)) + 128

    if new_value > 255:
        new_value = 255
    if new_value < 0:
        new_value = 0

    return new_value


#
def set_contrast_1(img, contrast_value):
    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    # if contrast_method not in contrasts:
    #   raise Exception('')

    for i in range(0, height):
        for j in range(0, width):

            R = matrix[i][j][0]
            G = matrix[i][j][1]
            B = matrix[i][j][2]

            R = contrast_formula_1(contrast_value, R)
            G = contrast_formula_1(contrast_value, G)
            B = contrast_formula_1(contrast_value, B)

            matrix[i][j] = [R, G, B]

    matrix = Image.fromarray(np.uint8(matrix))
    return matrix

# -------------------------------------------------------------


#
def contrast_formula_2(contrast_value, RGB_brightness_value, RGB_component):
    new_value = (contrast_value * (RGB_component - RGB_brightness_value)) + RGB_brightness_value

    if new_value > 255:
        new_value = 255
    if new_value < 0:
        new_value = 0

    return new_value


# limit to -255 to 255
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
def set_contrast_2(img, contrast_value):

    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    brightness_vector = get_brightness_value(matrix, height, width)
    R_brightness_value = brightness_vector[0]
    G_brightness_value = brightness_vector[1]
    B_brightness_value = brightness_vector[2]

    for i in range(0, height):
        for j in range(0, width):

            R = matrix[i][j][0]
            G = matrix[i][j][1]
            B = matrix[i][j][2]

            R = contrast_formula_2(contrast_value, R_brightness_value, R)
            G = contrast_formula_2(contrast_value, G_brightness_value, G)
            B = contrast_formula_2(contrast_value, B_brightness_value, B)

            matrix[i][j] = [R, G, B]

    matrix = Image.fromarray(np.uint8(matrix))
    return matrix


# -------------------------------------------------------------
my_img = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
my_img.show()
contrast_image = set_contrast_2(my_img, 10)
contrast_image.show()


'''
- add comments
- check the range for every function
- add raise exception 
'''






