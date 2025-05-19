## REVERSE
n = int(input()[::-1])

print(n)

## STRANGE ARRAY
n = int(input())
arr = sorted([int(i) for i in input().split()])

for i in range(1, n, 2):
    arr[i], arr[i - 1] = arr[i - 1], arr[i]

print(*arr)