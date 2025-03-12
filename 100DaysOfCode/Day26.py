#Tribonacci Series
def tri(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 1
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        x = 0
        y = 1
        z = 1
        
        for i in range(3, n + 1):
            x, y, z = y, z, x + y + z
            
        return z        



#Factorial Trailing Zeroes
def trailingZeroes(N):
    if N < 5:
        return 0
    return N // 5 + trailingZeroes(N // 5)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def helper(n):
            if n<5:
                return 0
            return n//5 + helper(n//5)
        return helper(n)