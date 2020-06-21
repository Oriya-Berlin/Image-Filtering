# put all relevant vectors on a list
# make average for every component
# calculate median for evey component
# return vector that represent pixel
import numpy as np
from PIL import Image


# take a pixel with all the pixels around him and flat it to array
def flat_matrix(matrix, x, y):  #need to take care that function: index out of bounds
    _list = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            _list.append(matrix[i, j])
    return _list


# take a pixel from matrix *frame* with all the pixels around him and flat it to array
def flat_matrix_frame(matrix, x, y):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    _list = []

    if x == 0:
        if y == 0:
            _list.append(matrix[x, y]), _list.append(matrix[x, y+1])
            _list.append(matrix[x+1, y+1]), _list.append(matrix[x+1, y])
            return _list
        elif y == width:
            pass  # real pass
        else:
            _list.append(matrix[x, y]), _list.append(matrix[x, y+1])
            _list.append(matrix[x+1, y+1]), _list.append(matrix[x+1, y])
            _list.append(matrix[x+1, y-1]), _list.append(matrix[x, y-1])
            return _list

    if y == 0:
        if x == 0:
            pass  # real pass
        elif x == height:
            _list.append(matrix[x, y]), _list.append(matrix[x-1, y])
            _list.append(matrix[x - 1, y + 1]), _list.append(matrix[x, y+1])
            return _list
        else:
            _list.append(matrix[x, y]), _list.append(matrix[x-1, y])
            _list.append(matrix[x-1, y+1]), _list.append(matrix[x, y+1])
            _list.append(matrix[x+1, y+1]), _list.append(matrix[x+1, y])
            return _list

    if x == height:
        if y == 0:
            pass  # real pass
        elif y == width:
            _list.append(matrix[x, y]), _list.append(matrix[x-1, y])
            _list.append(matrix[x-1, y-1]), _list.append(matrix[x, y-1])
            return _list
        else:
            _list.append(matrix[x, y]), _list.append(matrix[x, y-1])
            _list.append(matrix[x-1, y-1]), _list.append(matrix[x-1, y])
            _list.append(matrix[x-1, y+1]), _list.append(matrix[x, y+1])
            return _list

    if y == width:
        if x == height:
            pass  # real pass
        elif x == 0:
            _list.append(matrix[x, y]), _list.append(matrix[x, y-1])
            _list.append(matrix[x+1, y-1]), _list.append(matrix[x+1, y])
            return _list
        else:
            _list.append(matrix[x, y]), _list.append(matrix[x+1, y])
            _list.append(matrix[x+1, y-1]), _list.append(matrix[x, y-1])
            _list.append(matrix[x-1, y-1]), _list.append(matrix[x-1, y])
            return _list


# return the median vector(RGB) in array of pixels, good for RGB scales
def calculate_median_pixel(pixels_list):
    R, G, B = [], [], []

    for pixel in pixels_list:
        R.append(pixel[0])
        G.append(pixel[1])
        B.append(pixel[2])

    R = median(R)
    G = median(G)
    B = median(B)
    median_pixel = [R, G, B]
    return median_pixel


# return the median value in array, good for Grey scale
def median(_list):
    sorted_list = sorted(_list)
    n = len(sorted_list)
    return sorted_list[n//2]


# iterate only at he matrix frame, and clean the noises
def clean_frame_sp(matrix, height, width):

    for top in range(width):
        if all(matrix[0][top] == np.array([0, 0, 0])) or all(matrix[0][top] == np.array([255, 255, 255])):
            sub_matrix = flat_matrix_frame(matrix, 0, top)
            median_pixel = calculate_median_pixel(sub_matrix)
            matrix[0][top] = median_pixel


    for left in range(1, height - 1):
        if all(matrix[left][0] == np.array([0, 0, 0])) or all(matrix[left][0] == np.array([255, 255, 255])):
            sub_matrix = flat_matrix_frame(matrix, left, 0)
            median_pixel = calculate_median_pixel(sub_matrix)
            matrix[left][0] = median_pixel


    for right in range(1, height - 1):
        if all(matrix[right][width-1] == np.array([0, 0, 0])) or all(matrix[right][width-1] == np.array([255, 255, 255])):
            sub_matrix = flat_matrix_frame(matrix, right, width - 1)
            median_pixel = calculate_median_pixel(sub_matrix)
            matrix[right][width - 1] = median_pixel


    for bottom in range(width):
        if all(matrix[height-1][bottom] == np.array([0, 0, 0])) or all(matrix[height-1][bottom] == np.array([255, 255, 255])):
            sub_matrix = flat_matrix_frame(matrix, height - 1, bottom)
            median_pixel = calculate_median_pixel(sub_matrix)
            matrix[height - 1][bottom] = median_pixel

    return matrix


# iterate n-1 on m-1 internal matrix
def clean_internal_sp(matrix, height, width):
    for i in range(1, height-1):  # height
        for j in range(1, width-1):  # width
            if all(matrix[i][j] == np.array([0, 0, 0])) or all(matrix[i][j] == np.array([255, 255, 255])):

                sub_matrix = flat_matrix(matrix, i, j)
                median_pixel = calculate_median_pixel(sub_matrix)
                matrix[i][j] = median_pixel
    return matrix


# cleans salt and pepper noise from all the matrix
def clean_sp(img):

    clean_matrix = np.asarray(img, dtype='int32')
    size = clean_matrix.shape
    height, width = size[0], size[1]

    clean_matrix = clean_internal_sp(clean_matrix, height, width)
    clean_matrix = clean_frame_sp(clean_matrix, height, width)
    cleaned_matrix = Image.fromarray(np.uint8(clean_matrix))

    return cleaned_matrix


im = Image.open('/home/berlin/Desktop/250.bmp')
im = im.convert('RGB')
xr = clean_sp(im)
xr.show()