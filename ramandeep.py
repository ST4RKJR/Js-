# Given matrix A (NxM) 

N,M  = map(int,input().split())
matrix = []
for i in range(N):
    elements = list(map(int,input().split()))
    matrix.append(elements)

print(matrix)
    