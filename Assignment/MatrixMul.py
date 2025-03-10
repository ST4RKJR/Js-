def matrixMul(a,b):
    matrix = []
    n = 3
    for i in range(3):
        row = []
        for j in range(3):
            row.append(0)
        matrix.append(row)
    
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matrix[i][j] = a[i][k] * b[k][j]
    print(matrix)
matrixMul([2,3,4],[4,3,3])