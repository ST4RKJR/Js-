#Closest Prime Numbers in Range
def closestPrimes(left, right):
    # Sieve of Eratosthenes to find all prime numbers up to right
    is_prime = [True] * (right + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(right**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, right + 1, i):
                is_prime[j] = False

    # Collect primes in the given range
    primes = [i for i in range(left, right + 1) if is_prime[i]]

    # Find the closest pair
    if len(primes) < 2:
        return [-1, -1]

    min_diff = float('inf')
    res = [-1, -1]

    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] < min_diff:
            min_diff = primes[i + 1] - primes[i]
            res = [primes[i], primes[i + 1]]

    return res

# Example Usage
left, right = map(int, input().split())
print(*closestPrimes(left, right))