#Partition Equal Subset Sum
def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

# Example usage:
n = int(input())
nums = list(map(int, input().split()))
print(canPartition(nums))

class Solution:
    def canPartition(self, nums) -> bool:
        def subset_sum(nums,tar):
            n=len(nums)
            t=[[False] *(tar+1) for i in range(n+1)]

            for i in range(n+1):
                for j in range(tar+1):
                    if i==0:
                        t[i][j]=False
                    if j==0:
                        t[i][j]=True

            for i in range(1,n+1):
                for j in range(1,tar+1):
                    if nums[i-1]<=j:
                        t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]          
            return t[n][tar]
        sumi=sum(nums)
        if sumi%2!=0:
            return False
        else:
            return subset_sum(nums,sumi//2)
        
        
#Frog Jump (DP)
d={}
def frogJump(heights,i=-1):
    # Write your code here
    if i in d:
        return d[i]
    if i == -1:
        d[0]=0
        if len(heights)>1:
            d[1] = abs(heights[0]-heights[1])

        i = len(heights)-1
    if i == 0 :
        return 0
    if i == 1:
        return abs(heights[0]-heights[1])
    a = frogJump(heights,i-1)+abs(heights[i]-heights[i-1])
    b= frogJump(heights,i-2)+abs(heights[i]-heights[i-2])
    d[i] = min(a,b)
    return min(a,b)


class Solution:
    def maxProfit(self, prices) -> int:
        min_price = float('inf')
        max_profit = 0
        for current_price in prices:
            min_price = min(current_price, min_price)
            max_profit = max(max_profit, current_price - min_price)   
        return max_profit