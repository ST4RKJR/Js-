def col_sum(mat):
    n = len(mat)        # number of rows
    m = len(mat[0])     # number of columns

    max_val = -1
    col_index = -1

    # Step 1: Find max element and its column index
    for i in range(n):
        for j in range(m):
            if mat[i][j] > max_val:
                max_val = mat[i][j]
                col_index = j

    # Step 2: Sum all elements in that column
    total = 0
    for i in range(n):
        total += mat[i][col_index]

    return total
