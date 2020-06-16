import numpy as np
from PIL import Image
from tests import *

class Img:

    def __init__(self, path):

        self.path = path
        self.img = Image.open(self.path)
        self.width, self.height = self.img.size
        self.matrix = self.img.load()

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def show(self):
        self.img.show()

g = Img('/home/berlin/Desktop/index.jpeg')

print(g.get_width())
print(g.get_height())
print(g.matrix[150,1])
g.matrix[150,1] = (0,0,250)
print(g.matrix[150,1])
#g.show()

img_4 = Image.open('/home/berlin/Desktop/250.bmp')

img_4.convert("RGB")
i = img_4.load()
print(i[50, 50])
x = clean_sp(img_4)
x.show()
