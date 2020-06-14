# put all relevant vectors on a list
# make average for every component
# calculate median for evey component
# return vector that represent pixel


#
def flat_matrix(matrix, x, y):
    _list = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            _list.append(matrix[i, j])
    return _list


#
def calculate_median_pixel(pixels_list):  # its need to return vector
    R, G, B = [], [], []

    for pixel in pixels_list:
        R.append(pixel[0])
        G.append(pixel[1])
        B.append(pixel[2])

    R = median(R)
    G = median(G)
    B = median(B)
    median_pixel = (R, G, B, 255)  # RGBA?
    return median_pixel


#
def median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    return sorted_list[n//2]


# cleans salt and pepper noise
def clean_sp(img):
    width, height = img.size
    matrix = img.load()  # i wonder if i need to use the clean matrix or the original matrix
    clean_img = img.copy()
    clean_matrix = clean_img.load()
    i = 0  #
    for i in range(1, width-1):
        for j in range(1, height-1):
            #if clean_matrix[i, j] == (0, 0, 0, 255):
            #   print(clean_matrix[i, j])
            #    print(i)
            #    i += 1
            if clean_matrix[i, j] == (0, 0, 0,255) or clean_matrix[i, j] == (255, 255,255, 255):

                small_matrix = flat_matrix(matrix, i, j)
                print(small_matrix)
                median_pixel = calculate_median_pixel(small_matrix)
                clean_matrix[i, j] = median_pixel
                print(median_pixel)
    return clean_img








