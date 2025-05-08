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
    
    
#Smallest Prime Factor of X
def smallest_prime_factor(n):
    spf = list(range(n + 1))  
    for i in range(2, int(n**0.5) + 1):
        if spf[i] == i:  
            for j in range(i * i, n + 1, i):
                if spf[j] == j:  
                    spf[j] = i  
    return spf

N = int(input())
arr = list(map(int, input().split()))
max_val = max(arr)
spf = smallest_prime_factor(max_val)
print(*[spf[num] for num in arr])