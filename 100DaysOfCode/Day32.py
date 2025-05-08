#
def countGoodNumbers(n):
    MOD = 10**9 + 7
    even_digits = 5  # {0, 2, 4, 6, 8}
    prime_digits = 4  # {2, 3, 5, 7}

    even_positions = (n + 1) // 2
    odd_positions = n // 2

    return pow(even_digits, even_positions, MOD) * pow(prime_digits, odd_positions, MOD) % MOD

def findTheWinner(n, k):
    friends = list(range(1, n + 1))
    index = 0
    
    while len(friends) > 1:
        index = (index + k - 1) % len(friends)
        friends.pop(index)
    
    return friends[0]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float('inf')
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]
