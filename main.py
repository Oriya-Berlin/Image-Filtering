import numpy as np
from PIL import Image


width = 8
height = 4

# { ( [][][] ) , ( [][][] ) , ( [][][] ) , ( [][][] ) }  height, width, pixel
array = np.zeros([height, width, 3], dtype=np.uint8)
print(array)
array[:, :] = [255, 128, 0]
print(array)


img = Image.fromarray(array)
img.save('/home/berlin/Desktop/test.png')

# ----------------------------------------------------------------

array_2 = np.zeros([100, 200, 3], dtype=np.uint8)

array_2[:, 0:100] = [150, 150, 150]
array_2[:, 100:200] = [255, 255, 255]

img_2 = Image.fromarray(array_2)
img_2.save('/home/berlin/Desktop/test.png')

# ----------------------------------------------------------------

array_3 = np.zeros([100, 200, 4], dtype=np.uint8)
array_3[:, :100] = [255, 128, 0, 255] #Orange left side
array_3[:, 100:] = [0, 0, 255, 255]   #Blue right side

# Set transparency depending on x position
for x in range(200):
    for y in range(100):
        array_3[y, x, 3] = x  # this is how we acesess to 'alpha' value
        #print(x)

img = Image.fromarray(array_3)
img.save('/home/berlin/Desktop/testrgba.png')

# ----------------------------------------------------------------

img_4 = Image.open('/home/berlin/Desktop/test.png')
array_4 = np.array(img_4)


array_4[50, 50] = [0,0,255]
array_4[50, 49] = [0,0,255]
array_4[50, 48] = [0,0,255]
array_4[50, 47] = [0,0,255]
array_4[50, 46] = [0,0,255]
array_4[50, 45] = [0,0,255]
array_4[50, 44] = [0,0,255]
p = array_4[50, 44]
print()


test = Image.fromarray(array_4)
test.save('/home/berlin/Desktop/test0.png')
print(array_4.shape)

for height in range(225):
    for width in range(340):
        #array_4[height, width, 3] =
        pass