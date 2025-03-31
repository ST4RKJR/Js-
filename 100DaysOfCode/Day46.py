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
