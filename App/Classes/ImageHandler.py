import numpy as np
from PIL import Image


# this class will hold all image manipulation functions
class ImageHandler:

    def __init__(self, url):
        self.url = url
        self.image = Image.open(url)
        self.matrix = np.asarray(self.image, dtype='int32')
        self.size = self.matrix.shape
        self.height = self.size[0]
        self.width = self.size[1]
        # TODO: we also need to add stack to the object, maybe we need to add that in separate class

    def getImage(self):
        return self.image

    def getMatrix(self):
        return self.matrix

    def getSize(self):
        return self.size

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width
