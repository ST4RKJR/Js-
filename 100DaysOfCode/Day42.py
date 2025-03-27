#GReatest Sum Divisible by three
def maxSumDivThree(nums):
    dp = [0, 0, 0]
    
    for num in nums:
        temp = dp[:]
        for s in temp:
            dp[(s + num) % 3] = max(dp[(s + num) % 3], s + num)
    
    return dp[0]

# Example Usage
print(maxSumDivThree([3, 6, 5, 1, 8]))  # Output: 18
print(maxSumDivThree([4]))              # Output: 0