import numpy as np
from PIL import Image


# this class will hold all image manipulation functions
class ImageHandler:



    def __init__(self, url):
        self.url = url
        self.original_image = Image.open(url)
        self.image_copy = self.original_image
        self.matrix = np.asarray(self.original_image, dtype='int32')
        self.size = self.matrix.shape
        self.height = self.size[0]
        self.width = self.size[1]

    def get_original_image(self):
        return self.original_image

    def getMatrix(self):
        return self.matrix

    def getSize(self):
        return self.size

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
