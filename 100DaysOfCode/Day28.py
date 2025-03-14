#Minimum Jumps
def min_jumps(n, arr):
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1
    
    jumps = 0
    max_reach = 0
    step = 0
    last_jump = 0
    
    for i in range(n):
        max_reach = max(max_reach, i + arr[i])
        
        if i == last_jump:
            if max_reach <= i:
                return -1
            jumps += 1
            last_jump = max_reach
            if last_jump >= n - 1:
                return jumps
            
    return -1

n = int(input())
arr = list(map(int, input().split()))
print(min_jumps(n, arr))

class Solution:
    def jump(self, nums):
        jumps, currentEnd, farthest = 0, 0, 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                jumps += 1
                currentEnd = farthest
        return jumps
    
#House Robber 2
def rob_linear(nums):
    prev, curr = 0, 0
    for num in nums:
        prev, curr = curr, max(curr, prev + num)
    return curr

def rob_circular(nums):
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

n = int(input())
nums = list(map(int, input().split()))
print(rob_circular(nums))