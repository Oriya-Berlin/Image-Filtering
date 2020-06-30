import numpy as np
from PIL import Image


#  i need to check if i can make one convolution to internal and matrix frame  with 'if None' [?]
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


# making convolution on matrix frame only
def frame_convolution(matrix, kernel):
    pass


# making convolution on internal n-1 * m-1 matrix
def internal_convolution(original_matrix, kernel, height, width, new_matrix):  # kernel(matrix) == filter

    for i in range(1, height-1):
        for j in range(1, width-1):
            new_RGB_vector = calculate_internal_convolution(original_matrix, kernel, i, j)
            new_matrix[i][j] = new_RGB_vector

    return new_matrix


#  this function will get filter(kernel matrix), and return, filtered image
def image_filtering(img, filter):

    original_matrix = np.asarray(img, dtype='int32')
    new_matrix = original_matrix.copy()
    size = original_matrix.shape
    height, width = size[0], size[1]
    new_matrix = internal_convolution(original_matrix, filter, height, width, new_matrix)

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
