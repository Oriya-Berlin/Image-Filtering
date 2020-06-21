import  numpy as np
from PIL import Image

colors = ('red', 'blue', 'green')
# need to add the tuple 'colors' to the parameters


def color_filtering(img):
    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):  # height
        for j in range(0, width):
            '''
            R = matrix[i][j][0]
            if R < 0:
                R = 0
            G = matrix[i][j][1] - 255
            if G < 0:
                G = 0
            B = matrix[i][j][2] - 255
            if B < 0:
                B = 0
            '''
            R = 0
            G = 0
            B = matrix[i][j][2]
            matrix[i][j] = [R, G, B]


    filtered_img = Image.fromarray(np.uint8(matrix))
    return filtered_img


my_img = Image.open('/home/berlin/Desktop/index.jpeg')
new_image = color_filtering(my_img)
new_image.show()












