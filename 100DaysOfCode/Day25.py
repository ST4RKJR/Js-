#Maximum Absolute Sum of Array Subarrays
def maxAbsoluteSum(nums):
    max_sum = min_sum = total_max = total_min = 0
    for num in nums:
        max_sum = max(num, max_sum + num)
        min_sum = min(num, min_sum + num)
        total_max = max(total_max, max_sum)
        total_min = min(total_min, min_sum)
    return max(total_max, abs(total_min))

#Count Even Factors
n = int(input())
count = 0
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        if i % 2 == 0:
            count += 1
        if (n // i) % 2 == 0 and i != n // i:
            count += 1
print(count)