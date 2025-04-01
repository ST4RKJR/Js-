#Climbing Stairs (DP)
def climb(x):
    a , b = 1 ,1 
    for i in range(x):
        a ,b = b , (a+b) % ((10**9)+7) 
    return a

x = int(input())
print(climb(x))

#Find TargetSumWays 
def findTargetSumWays(nums, target):
    from collections import defaultdict
    
    dp = defaultdict(int)
    dp[0] = 1  # Base case: one way to make sum 0 (using no elements)
    
    for num in nums:
        next_dp = defaultdict(int)
        for summation in dp:
            next_dp[summation + num] += dp[summation]
            next_dp[summation - num] += dp[summation]
        dp = next_dp  # Move to the next iteration
    
    return dp[target]

class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        # Calculate the total sum of nums
        total_sum = sum(nums)

        # Edge case: if target is out of bounds of achievable sums
        if target > total_sum or (total_sum - target) % 2 != 0:
            return 0

        # The actual sum we need to find in subset (derived from equation)
        s = (total_sum - target) // 2

        # Initialize the DP table where dp[j] is the number of ways to sum to j
        dp = [0] * (s + 1)
        dp[0] = 1  # There's one way to get sum 0, by choosing nothing

        # Update dp table for each number in nums
        for num in nums:
            for j in range(s, num - 1, -1):  # Traverse backward to avoid overwriting
                dp[j] += dp[j - num]

        return dp[s]