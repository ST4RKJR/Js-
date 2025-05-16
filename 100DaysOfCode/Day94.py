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
    
    
## CLOSEST PRIME NUMBERS IN RANGE
def closestPrimes(left, right):
    
    primes = [1] * (right + 1)
    primes[0] = primes[1] = 0
    p = 2
    while p * p <= right:
        if primes[p]:
            for i in range(p * p, right + 1, p):
                primes[i] = 0
        p += 1
    
    prr = [i for i in range(left, right + 1) if primes[i]]
    min_len = float("inf")
    ans = [-1, -1]

    if len(prr) < 2:
        return ans

    for i in range(len(prr) - 1):
        if min_len > prr[i + 1] - prr[i]:
            ans = [prr[i], prr[i + 1]]
            min_len = prr[i + 1] - prr[i]
    return ans