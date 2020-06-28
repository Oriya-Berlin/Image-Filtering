import numpy as np
from PIL import Image


# that function will detect edges, as edge_value get close to 0, we will get more differences
def edge_detection(img, edge_value):

    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):
        for j in range(0, width-1):

            R = matrix[i][j][0]
            G = matrix[i][j][1]
            B = matrix[i][j][2]

            R_next = matrix[i][j+1][0]
            G_next = matrix[i][j+1][1]
            B_next = matrix[i][j+1][2]

            if abs(R - R_next) > edge_value and abs(G - G_next) > edge_value and abs(B - B_next) > edge_value:
                matrix[i][j] = [0, 255, 0]
            else:
                matrix[i][j] = [0, 0, 0]

    image = Image.fromarray(np.uint8(matrix))
    return image


'''
img_7 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/f2.jpg')
img_7.show()
edge_detected_image = edge_detection(img_7, 15)
edge_detected_image.show()
'''



