import numpy as np
from PIL import Image


class Img:

    def __init__(self, path):

        self.path = path
        self.img = Image.open(self.path)
        self.width, self.height = self.img.size

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

g = Img('/home/berlin/Desktop/test0.png')

print(g.get_width())
print(g.get_height())
