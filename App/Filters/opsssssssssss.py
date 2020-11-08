
import numpy as np
from PIL import Image

# in testing....
def ops(img):

    matrix = np.asarray(img, dtype='int32')
    size = matrix.shape
    height, width = size[0], size[1]

    for i in range(0, height):
        for j in range(0, width):

            if i%2 == 0:
                if j%100 == 0:
                    matrix[i][j] = [255, 0, 0]  # [0, 0, 0]

            else:
                if j%100 != 0:
                    matrix[i][j] = [255, 0, 0]













    image = Image.fromarray(np.uint8(matrix))
    return image



img_7 = Image.open('/home/berlin/PycharmProjects/Image Processing/images/f2.jpg')
img_7.show()
edge_detected_image = ops(img_7)
edge_detected_image.show()





