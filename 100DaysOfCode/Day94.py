## CHOCOLATY PROBLEM
prr = []
for i in range(2, 31624):
    for j in prr:
        if i % j == 0:
            break
    else:
        prr.append(i)

n = int(input())
k = 2 if n == 2 else n | 1
while True:
    for p in prr:
        if p * p > k:
            print(k - n)
            exit()
        if k % p == 0:
            break
    else:
        print(k - n)
        exit()
    k += 2