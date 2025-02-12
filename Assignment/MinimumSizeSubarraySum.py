def min_subarray_len(target, nums):
    n = len(nums)
    left = 0
    curr_sum = 0
    min_len = float('inf')

    for right in range(n):
        curr_sum += nums[right]

        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    print(min_len if min_len != float('inf') else 0)

target = int(input())
nums = list(map(int, input().split()))
min_subarray_len(target, nums)