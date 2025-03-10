#Maximum Absolute Sum of Array Subarrays
def maxAbsoluteSum(nums):
    max_sum = min_sum = total_max = total_min = 0
    for num in nums:
        max_sum = max(num, max_sum + num)
        min_sum = min(num, min_sum + num)
        total_max = max(total_max, max_sum)
        total_min = min(total_min, min_sum)
    return max(total_max, abs(total_min))