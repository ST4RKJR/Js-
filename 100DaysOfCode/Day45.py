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

#Check if Prime 
def sieve(limit):
    primes = [1] * (limit + 1)
    primes[0] = primes[1] = 0  
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = 0
    return primes

N = int(input())
arr = list(map(int, input().split()))

prime_lookup = sieve(10**6)

print(" ".join(str(prime_lookup[num]) for num in arr))


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left > right:
            return [-1, -1]

        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(left, right + 1) if is_prime[i]]


        if len(primes) < 2:
            return [-1, -1]

        min_diff, num1, num2 = float('inf'), -1, -1
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                num1, num2 = primes[i - 1], primes[i]

        return [num1, num2]