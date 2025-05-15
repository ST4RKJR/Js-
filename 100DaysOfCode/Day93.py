## PRINT THE MATRIX
n = int(input())
mat = []
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)

for i in range(n):
    print(*mat[i])
    
## MINIMUM DIFFRENCE
n = int(input())
arr = [int(i) for i in input().split()]

arr.sort()
target = arr[n // 2]

ans = 0
for i in arr:
    ans += abs(i - target)

print(ans)    