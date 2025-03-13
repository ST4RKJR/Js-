#Min Cost Climbing Stairs
def minCostClimbingStairs(cost):
    cost.append(0)
        
    for i in range(len(cost) - 4, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
        
    return min(cost[0], cost[1])

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
    
    
#House Of Robbers
def recurse(nums,i):
    #base case 
    if i >= len(nums):
        return 0
    #recursive Step
    chori_karo = nums[i] + recurse(nums,i+2)
    abhi_chori_mat_karo = 0 + recurse(nums,i+1)
    return max(chori_karo,abhi_chori_mat_karo)



def rob(nums):      
    return recurse(nums,0)

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] 