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



def min_time(times, totalTrips):
    def trips_completed_in_time(mid):
        # Calculate total trips that can be completed within time `mid`
        return sum(mid // t for t in times)
    
    low, high = 1, min(times) * totalTrips  # Initialize search space
    while low < high:
        mid = (low + high) // 2
        if trips_completed_in_time(mid) >= totalTrips:
            high = mid  # Adjust upper bound
        else:
            low = mid + 1  # Adjust lower bound
    
    return low  # Minimum time required

# Example Usage:
N, totalTrips = map(int, input().split())  # Number of buses and total trips
times = list(map(int, input().split()))  # Time taken by each bus
print(min_time(times, totalTrips))
