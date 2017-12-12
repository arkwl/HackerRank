def transpose_matrix(matrix):
    if(len(matrix)>1):
        print(matrix)
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                if i == j:
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp

        print(matrix)

transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
