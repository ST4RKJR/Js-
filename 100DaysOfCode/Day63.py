def compute_smallest_prime_factors(max_num):
    spf = list(range(max_num + 1))  # Smallest prime factor for every number
    for i in range(2, int(max_num ** 0.5) + 1):
        if spf[i] == i:  # `i` is a prime
            for j in range(i * i, max_num + 1, i):
                if spf[j] == j:  # Mark the smallest prime factor
                    spf[j] = i
    return spf

def smallest_prime_factors(arr):
    max_num = max(arr)
    spf = compute_smallest_prime_factors(max_num)
    return [spf[num] for num in arr]

# Input
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # Array elements

# Output
result = smallest_prime_factors(arr)
print(" ".join(map(str, result)))
