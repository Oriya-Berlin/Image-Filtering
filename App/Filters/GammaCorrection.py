import numpy as np
from PIL import Image


"""
- by default, gamma value equal to ~ 0.45, and as gamma value go to 0
  it will increase the quality of shadow in the image.

- formula:  ƒ(i,j) <-- 255 * ( ƒ(i,j)/255 )^(gamma)
"""


CONST_GAMMA = 1/2.2


# generate gamma value according to the formula on the top
def generate_gamma_correction(RGB_component, gamma_value):
    generated_component = 255 * (pow(RGB_component/255, gamma_value))
    return generated_component


# set gamma value on every RGB vector component
def set_gamma_correction(img, gamma_value=CONST_GAMMA):

    if gamma_value < 0:
        raise Exception('gamma value must to be at greater or equal to 0.')

    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):
        for j in range(0, width):
            R = generate_gamma_correction(matrix[i][j][0], gamma_value)
            G = generate_gamma_correction(matrix[i][j][1], gamma_value)
            B = generate_gamma_correction(matrix[i][j][2], gamma_value)
            matrix[i][j] = [R, G, B]

    generated_image = Image.fromarray(np.uint8(matrix))
    return generated_image

'''
img_6 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/dark.jpeg')
img_6.show()
corrected_image = set_gamma_correction(img_6, 5)
corrected_image.show()
'''








