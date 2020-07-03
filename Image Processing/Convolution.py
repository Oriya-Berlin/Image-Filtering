import numpy as np
from PIL import Image


#  will calculate the convolution for every pixel in the internal matrix [n-1 on m-1]
def calculate_internal_convolution(original_matrix, kernel, i, j):
    new_RGB_vector = []

    for RGB in range(0, 3):
        new_RGB_value = original_matrix[i-1][j-1][RGB] * kernel[0][0] + \
                        original_matrix[i-1][j][RGB] * kernel[0][1] + \
                        original_matrix[i-1][j+1][RGB] * kernel[0][2] + \
                        original_matrix[i][j-1][RGB] * kernel[1][0] + \
                        original_matrix[i][j][RGB] * kernel[1][1] + \
                        original_matrix[i][j+1][RGB] * kernel[1][2] + \
                        original_matrix[i+1][j - 1][RGB] * kernel[2][0] + \
                        original_matrix[i+1][j][RGB] * kernel[2][1] + \
                        original_matrix[i+1][j+1][RGB] * kernel[2][2]

        if new_RGB_value > 255:
            new_RGB_value = 255

        if new_RGB_value < 0:
            new_RGB_value = 0

        new_RGB_vector.append(new_RGB_value)

    return new_RGB_vector


# will calculate the convolution on matrix frame only
def calculate_frame_convolution(original_matrix, kernel, x, y):
    height = len(original_matrix) - 1
    width = len(original_matrix[0]) - 1
    new_RGB_vector = []

    if x == 0:
        if y == 0:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x][y+1][RGB] * kernel[1][2] + \
                                original_matrix[x+1][y+1][RGB] * kernel[2][2] + \
                                original_matrix[x+1][y][RGB] * kernel[2][1]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

        elif y == width:
            pass  #

        else:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x][y+1][RGB] * kernel[1][2] + \
                                original_matrix[x+1][y+1][RGB] * kernel[2][2] + \
                                original_matrix[x+1][y][RGB] * kernel[2][1] + \
                                original_matrix[x+1][y-1][RGB] * kernel[2][0] + \
                                original_matrix[x][y-1][RGB] * kernel[1][0]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector


    if y == 0:
        if x == 0:
            pass  #
        elif x == height:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x-1][y][RGB] * kernel[0][1] + \
                                original_matrix[x-1][y+1][RGB] * kernel[0][2] + \
                                original_matrix[x][y+1][RGB] * kernel[1][2]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

        else:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x-1][y][RGB] * kernel[0][1] + \
                                original_matrix[x-1][y+1][RGB] * kernel[0][2] + \
                                original_matrix[x][y+1][RGB] * kernel[1][2] + \
                                original_matrix[x+1][y+1][RGB] * kernel[2][2] + \
                                original_matrix[x+1][y][RGB] * kernel[2][1]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

    if x == height:
        if y == 0:
            pass  #
        elif y == width:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x][y-1][RGB] * kernel[1][0] + \
                                original_matrix[x-1][y-1][RGB] * kernel[0][0] + \
                                original_matrix[x-1][y][RGB] * kernel[0][1]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

        else:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x][y-1][RGB] * kernel[1][0] + \
                                original_matrix[x-1][y-1][RGB] * kernel[0][0] + \
                                original_matrix[x-1][y][RGB] * kernel[0][1] + \
                                original_matrix[x-1][y+1][RGB] * kernel[0][2] + \
                                original_matrix[x][y+1][RGB] * kernel[1][2]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

    if y == width:
        if x == height:
            pass  #
        elif x == 0:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x+1][y][RGB] * kernel[2][1] + \
                                original_matrix[x+1][y-1][RGB] * kernel[2][0] + \
                                original_matrix[x][y-1][RGB] * kernel[1][0]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector

        else:
            for RGB in range(0, 3):
                new_RGB_value = original_matrix[x][y][RGB] * kernel[1][1] + \
                                original_matrix[x+1][y][RGB] * kernel[2][1] + \
                                original_matrix[x+1][y-1][RGB] * kernel[2][0] + \
                                original_matrix[x][y-1][RGB] * kernel[1][0] + \
                                original_matrix[x-1][y-1][RGB] * kernel[0][0] + \
                                original_matrix[x-1][y][RGB] * kernel[0][1]

                if new_RGB_value > 255:
                    new_RGB_value = 255

                if new_RGB_value < 0:
                    new_RGB_value = 0

                new_RGB_vector.append(new_RGB_value)
            return new_RGB_vector


# iterate and making convolution on internal n-1 on m-1 matrix
def iterate_internal_matrix(original_matrix, kernel, height, width, new_matrix):  # kernel(matrix) == filter

    for i in range(1, height-1):
        for j in range(1, width-1):
            new_RGB_vector = calculate_internal_convolution(original_matrix, kernel, i, j)
            new_matrix[i][j] = new_RGB_vector

    return new_matrix


# iterate and making convolution on on the matrix frame
def iterate_frame_matrix(original_matrix, kernel, height, width, new_matrix):

    for top in range(width):
        new_RGB_vector = calculate_frame_convolution(original_matrix, kernel, 0, top)
        new_matrix[0][top] = new_RGB_vector

    for left in range(1, height - 1):
        new_RGB_vector = calculate_frame_convolution(original_matrix, kernel, left, 0)
        new_matrix[left][0] = new_RGB_vector

    for right in range(1, height - 1):
        new_RGB_vector = calculate_frame_convolution(original_matrix, kernel, right, width-1)
        new_matrix[right][width-1] = new_RGB_vector

    for bottom in range(width):
        new_RGB_vector = calculate_frame_convolution(original_matrix, kernel, height-1, bottom)
        new_matrix[height-1][bottom] = new_RGB_vector

    return new_matrix


#  this function will get filter(kernel matrix), and return, filtered image
def image_filtering(img, filter):

    original_matrix = np.asarray(img, dtype='int32')
    new_matrix = original_matrix.copy()
    size = original_matrix.shape
    height, width = size[0], size[1]
    new_matrix = iterate_internal_matrix(original_matrix, filter, height, width, new_matrix)
    new_matrix = iterate_frame_matrix(original_matrix, filter, height, width, new_matrix)
    image = Image.fromarray(np.uint8(new_matrix))
    return image


#  test
kernel1 = [[0, -1, 0],
           [-1, 5, -1],
           [0, -1, 0]]

'''
img_8 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/f1.jpg')
img_8.show()
#img_8 = img_8.convert('RGB')
filtered_image = image_filtering(img_8, kernel1)
filtered_image.show()
'''
