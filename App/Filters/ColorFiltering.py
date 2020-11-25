import numpy as np
from PIL import Image


colors = ('Red', 'Blue', 'Green')


def color_filtering(img, color):
    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    if color not in colors:
        raise Exception(' You must to choose valid color: "red"/"green"/"blue" ')

    if color == 'Red':
        for i in range(0, height):
            for j in range(0, width):
                R = matrix[i][j][0]
                G = 0
                B = 0
                matrix[i][j] = [R, G, B]

    if color == 'Green':
        for i in range(0, height):
            for j in range(0, width):
                R = 0
                G = matrix[i][j][1]
                B = 0
                matrix[i][j] = [R, G, B]

    if color == 'Blue':
        for i in range(0, height):
            for j in range(0, width):
                R = 0
                G = 0
                B = matrix[i][j][2]
                matrix[i][j] = [R, G, B]

    filtered_img = Image.fromarray(np.uint8(matrix))
    return filtered_img


'''
my_img = Image.open('/home/berlin/PycharmProjects/Image Processing/images/index.jpeg')
new_image = color_filtering(my_img, 'green')
new_image.show()
'''

