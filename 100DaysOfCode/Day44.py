#Range Prime
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def countPrimes(L, R):
    primes = sieve(R)
    return sum(primes[L:R + 1])


L, R = map(int, input().split())
print(countPrimes(L, R))


#Prime Pairs with Target Sum
def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def findPrimePairs(n):
    primes = sieve(n)
    result = []
    
    for x in range(2, n // 2 + 1):
        y = n - x
        if primes[x] and primes[y]:
            result.append([x, y])
    
    return result


primes = [False,False] + [True] * 999_999               #
                                                        #
for i in range(2, 1001):                                # <-- sieve construction
    if primes[i]:                                       # 
        for j in range(i + i, 1000_000, i):             #
            primes[j] = False                           #

class Solution:
    def findPrimePairs(self, n: int) :

        if n < 4: return []                             # 
                                                        # <-- edge cases
        if n%2 or n == 4:                               #
            return [[2,n-2]] if primes[n-2] else []     #

        return [[i, n - i] for i in range(3,(n+3)//2)   # <-- find pairs
                       if primes[i] and primes[n - i]]  #