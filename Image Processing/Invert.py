import numpy as np
from PIL import Image


def set_invert(img):

    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):
        for j in range(0, width):

            R = 255 - matrix[i][j][0]
            G = 255 - matrix[i][j][1]
            B = 255 - matrix[i][j][2]
            matrix[i][j] = [R, G, B]

    invert_image = Image.fromarray(np.uint8(matrix))
    return invert_image


'''
img_5 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
img_5.show()
inverted_image = set_invert(img_5)
inverted_image.show()
'''

