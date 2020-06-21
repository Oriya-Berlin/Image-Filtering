

"""
p = np.array([1,2,5])
x = np.array([1,2,3])
print(all(p==x))

# maybe the proble is with the small matrix calculation


m = [[['11'], ['12'], ['13']],
    [['21'], ['22'], ['23']],
    [['31'], ['32'], ['33']]]

print(len(m))
for i in range(0, 3):
    for j in range(0, 3):
        print(m[i][j])


#array[hight,width]
# it will create white img with height 3 and width 5
array_22 = np.zeros([3, 5, 3], dtype=np.uint8)
array_22[0:3, 0:5] = [255]


img = Image.fromarray(array_22)
img.save('/home/berlin/Desktop/testim.png')
print(len(array_22))
print(len(array_22[0]))
print(array_22)

for i in range(0, 3):
    for j in range(0, 5):
        print(array_22[i][j])
"""
m = [ [ ['11'], ['12'], ['13'], ['14'] ],
       [['21'], ['22'], ['23'], ['24'] ],
       [['31'], ['32'], ['33'], ['34'] ] ]

#print(m[0][1])
#print(len(m[0]))

