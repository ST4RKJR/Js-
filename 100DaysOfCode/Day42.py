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


class Solution:
    def maxSumDivThree(self, a) -> int:
        w = sum(a)
        if w%3 == 0:
            return w

        q = 0
        for v in a:
            q[v%3] = sorted(q[v%3]+[v])[:2]

        return w - min(q[w%3][0], sum(q[w%3%2+1]))
    
#Max Sum Non adjacent Numbers
def maxSum(n, nums):
    if n == 1:
        return nums[0]
    
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[-1]


