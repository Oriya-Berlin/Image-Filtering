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


#
def flat_matrix_frame(matrix, x, y):
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    _list = []

    if x == 0:
        if y == 0:
            pass
        elif y == width:
            pass  # real pass
        else:
            pass

    if y == 0:
        if x == 0:
            pass  # real pass
        elif x == height:
            pass
        else:
            pass

    if x == height:
        if y == 0:
            pass  # real pass
        elif y == width:
            pass
        else:
            pass

    if y == width:
        if x == height:
            pass  # real pass
        elif x == 0:
            pass
        else:
            pass



# return the median vector(RGB) in array of pixels, good for RGB scales
def calculate_median_pixel(pixels_list):  # its need to return vector
    R, G, B = [], [], []

    for pixel in pixels_list:
        R.append(pixel[0])
        G.append(pixel[1])
        B.append(pixel[2])

    R = median(R)
    G = median(G)
    B = median(B)
    median_pixel = [R, G, B] # RGBA?
    return median_pixel


# return the median value in array, good for Grey scale
def median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    return sorted_list[n//2]


# cleans salt and pepper noise
def clean_sp(img):

    matrix = np.asarray(img, dtype='int32')
    clean_matrix = np.asarray(img, dtype='int32')
    size = clean_matrix.shape
    height, width = size[0], size[1]

    for i in range(height):  # height
        for j in range(width): #width
            if all(clean_matrix[i][j] == np.array([0, 0, 0])) or all(clean_matrix[i][j] == np.array([255, 255, 255])):

                small_matrix = flat_matrix(matrix, i, j)
                median_pixel = calculate_median_pixel(small_matrix)
                clean_matrix[i][j] = median_pixel
    res = Image.fromarray(np.uint8(clean_matrix))
    return res


im = Image.open('/home/berlin/Desktop/250.bmp')
im = im.convert('RGB')
#x = clean_sp(im)
#x.show()

"""
p = np.array([1,2,5])
x = np.array([1,2,3])
print(all(p==x))

# maybe the proble is with the small matrix calculation


m = [[['11'], ['12'], ['13']],
    [['21'], ['22'], ['23']],
    [['31'], ['32'], ['33']]]

print(len(m))
for i in range(0, 3):
    for j in range(0, 3):
        print(m[i][j])


#array[hight,width]
# it will create white img with height 3 and width 5
array_22 = np.zeros([3, 5, 3], dtype=np.uint8)
array_22[0:3, 0:5] = [255]


img = Image.fromarray(array_22)
img.save('/home/berlin/Desktop/testim.png')
print(len(array_22))
print(len(array_22[0]))
print(array_22)

for i in range(0, 3):
    for j in range(0, 5):
        print(array_22[i][j])
"""
m = [ [ ['11'], ['12'], ['13'], ['14'] ],
       [['21'], ['22'], ['23'], ['24'] ],
       [['31'], ['32'], ['33'], ['34'] ] ]

print(m[0][1])
print(len(m[0]))

