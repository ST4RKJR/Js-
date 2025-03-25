#Climbing Stairs (DP)
def climbTree(n):
    a,b = 1,1
    for i in range(n):
        mod = 10**9
        a,b = b , (a+b) % (mod+7)
    return a 

n = int(input())
print(climbTree(n))


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n: int, memo: dict[int, int]) -> int:
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]


#Perfect squares Combinations
import math

def numSquares(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    
    return dp[N]