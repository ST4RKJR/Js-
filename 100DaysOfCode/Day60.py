target = int(input())
nums = list(map(int, input().split()))

min_length = float('inf')
left = 0
current_sum = 0

for right in range(len(nums)):
    current_sum += nums[right]
    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1

print(min_length if min_length != float('inf') else 0)