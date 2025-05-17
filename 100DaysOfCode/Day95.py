## SUM OF PRIMES

limit = 10 ** 6
p = 2
prr = [1] * (limit + 1)
prr[0] = prr[1] = 0

while p * p <= limit:
    if prr[p]:
        for i in range(p * p, limit + 1, p):
            prr[i] = 0
    p += 1

for _ in range(int(input())):
    n = int(input())
    if n < 4:
        print(-1)
        continue
    for x in range(2, n // 2 + 1):
        if prr[x] and prr[n - x]:
            print(x, n - x)
            break
    else:
        print(-1)