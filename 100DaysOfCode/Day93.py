## PRINT THE MATRIX
n = int(input())
mat = []
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)

for i in range(n):
    print(*mat[i])