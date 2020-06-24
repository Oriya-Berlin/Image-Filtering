import numpy as np
from PIL import Image


def set_brightness(img, brightness_value):
    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):
        for j in range(0, width):
            R = matrix[i][j][0] + brightness_value
            G = matrix[i][j][1] + brightness_value
            B = matrix[i][j][2] + brightness_value

            if R > 255: R = 255
            if R < 0: R = 0

            if G > 255: G = 255
            if G < 0: G = 0

            if B > 255: B = 255
            if B < 0: B = 0

            matrix[i][j] = [R, G, B]
    matrix = Image.fromarray(np.uint8(matrix))
    return matrix


'''
my_img = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
my_img.show()
bright_image = set_brightness(my_img, 60)
bright_image.show()
'''
