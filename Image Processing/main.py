import numpy as np
from PIL import Image
from tests import flat_matrix_frame

width = 8
height = 4

# { ( [][][] ) , ( [][][] ) , ( [][][] ) , ( [][][] ) }  height, width, pixel
array = np.zeros([height, width, 3], dtype=np.uint8)

img_0 = Image.open('/home/berlin/Desktop/test0.png')
data = np.asarray(img_0, dtype='int32')
data[20][20] = [0, 0, 0]

res = Image.fromarray(np.uint8(data))

#res.show()
#res.save('/home/berlin/Desktop/testtttt.png')


#print(data[0][0])
#print(data)

#print(array)
array[:, :] = [255, 128, 0]
#print(array)


#img = Image.fromarray(array)
#img.save('/home/berlin/Desktop/test.png')



# ----------------------------------------------------------------
"""
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
"""
test = [
        [['1'],  ['2'],  ['3'],  ['4'],  ['5']],
        [['6'],  ['7'],  ['8'],  ['9'],  ['10']],
        [['11'], ['12'], ['13'], ['14'], ['15']],
        [['16'], ['17'], ['18'], ['19'], ['20']],
        [['21'], ['22'], ['23'], ['24'], ['25']]
        ]
height = len(test)
width = len(test[0])
test = np.array(test, dtype=np.int32)
print('-----')

for top in range(width):
    #print(test[0][top])
    x = flat_matrix_frame(test, 0, top)
    print([l[0] for l in x])

for left in range(1, height-1):
    #print(test[left][0])
    x = flat_matrix_frame(test, left, 0)
    print([l[0] for l in x])

for right in range(1, height-1):
    #print(test[right][len(test[0])-1])
    x = flat_matrix_frame(test, right, width-1)
    print([l[0] for l in x])

for bottom in range(width):
    #print(test[len(test)-1][bottom])
    x = flat_matrix_frame(test, height-1, bottom)
    print([l[0] for l in x])
