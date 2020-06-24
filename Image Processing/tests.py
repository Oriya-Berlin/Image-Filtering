
m = [ [ ['11'], ['12'], ['13'], ['14'] ],
       [['21'], ['22'], ['23'], ['24'] ],
       [['31'], ['32'], ['33'], ['34'] ] ]

'''
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

'''

"""
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

"""
