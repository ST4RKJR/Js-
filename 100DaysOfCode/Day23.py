#Magical Array
def magicalArrays(arr):
    n = len(arr)
    count = 0
    i = 0

    while i < n:
        j = i
        while j < n and arr[j] == arr[i]:
            j += 1
        length = j - i
        count += (length * (length + 1)) // 2
        i = j

    return count

class Solution:
    def maximumGap(self, num):
        res = []
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            res.append(nums[i+1]-nums[i])
        return max(res)

#Maximum Gap
def maximumGap(nums):
    if not nums or len(nums) < 2:
        return 0

    min_val, max_val = min(nums), max(nums)
    if min_val == max_val:
        return 0

    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

    for num in nums:
        idx = (num - min_val) // bucket_size
        buckets[idx][0] = min(buckets[idx][0], num)
        buckets[idx][1] = max(buckets[idx][1], num)

    max_gap = 0
    prev_max = min_val

    for bucket in buckets:
        if bucket[0] == float('inf'):
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]

    return max_gap

N = int(input())
nums = list(map(int, input().split()))
print(maximumGap(nums))