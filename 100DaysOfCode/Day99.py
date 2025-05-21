## Cost of Stock 

n = int(input())
a = list(map(int, input().split()))
ans = []
l = 0

for r in range(1, n):
    if a[r] < a[r - 1]:
        if l < r - 1:
            ans.append((l, r - 1))
        l = r

if l < n - 1:
    ans.append((l, n - 1))

if not ans:
    print("null")
    exit()

for l, r in ans:
    print(l, r)
