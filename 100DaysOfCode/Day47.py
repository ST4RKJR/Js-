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
