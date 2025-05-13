## Spiral Matrix
n, m = map(int, input().split())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

result = []

top, bottom = 0, n - 1
left, right = 0, m - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    top += 1

    for i in range(top, bottom + 1):
        result.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1
        
    if left <= right:
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

print(*result)



#Matrix Z
n = int(input())
matrix = []
total = 0

for i in range(n):
    rows = list(map(int,input().split()))
    matrix.append(rows)

total += sum(matrix[0])
if n > 1 :
    total += sum(matrix[n-1])

for j in range(1,n-1):
    total += matrix[j][n-1-j]

print(total)