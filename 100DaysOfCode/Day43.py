#Sieve of Eratosthenes - Prime Number Generator
def sieve_of_eratosthenes(N):
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(N**0.5) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False
    print(*[i for i in range(N + 1) if primes[i]])

N = int(input())
sieve_of_eratosthenes(N)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return count
    
