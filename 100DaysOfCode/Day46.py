#XOR of primes (Contest)
def prime_xor(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    result = 0
    for i in range(2, n + 1):
        if primes[i]:
            result ^= i
    print(result)

n = int(input())
prime_xor(n)

#Prime Factors of X
def sieve_factorization(limit):
    spf = list(range(limit + 1))  
    for i in range(2, int(limit ** 0.5) + 1):
        if spf[i] == i:  
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i  
    return spf

def get_prime_factors(x, spf):
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    arr = list(map(int, data[1:N+1]))

    limit = 10**6
    spf = sieve_factorization(limit)

    results = []
    for num in arr:
        results.append(" ".join(map(str, get_prime_factors(num, spf))))
    
    sys.stdout.write("\n".join(results) + "\n")

solve()