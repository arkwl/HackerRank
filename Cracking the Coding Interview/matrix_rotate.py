import Queue

def rotate(matrix):
    print(matrix)

    for row in range(len(matrix)/2):
        tmp = Queue.Queue()
        size = len(matrix) - 1

        #top
        tmp.put(matrix[0][size])
        for i in range(size, 0, -1):
            matrix[0][i] = matrix[0][i-1]

        #right
        tmp.put(matrix[size][size])
        for j in range(size, 0, -1):
            if (j - 1 == 0):
                matrix[j][size] = tmp.get()
            else:
                matrix[j][size] = matrix[j-1][size]

        #bottom
        tmp.put(matrix[size][0])
        for i in range(0, size, 1):
            if (i + 1 == size):
                matrix[size][i] = tmp.get()
            else:
                matrix[size][i] = matrix[size][i+1]

        #left
        for i in range(0, size, 1):
            if (i + 1 == size):
                matrix[i][0] = tmp.get()
            else:
                matrix[i][0] = matrix[i+1][0]

    print(matrix)

print("1x1")
rotate([[1]])

print("2x2")
rotate([[1, 2],[3, 4]])

print("3x3")
rotate([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

print("4x4")
rotate([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])
