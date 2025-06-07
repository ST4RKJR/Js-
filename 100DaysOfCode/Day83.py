def max_sum(arr, K):
    N = len(arr)
    if K == 0:
        return 0
    
    # dp[i][k] = max sum using first i+1 elements with exactly k picks
    dp = [[float('-inf')] * (K + 1) for _ in range(N)]
    
    # Base cases
    dp[0][0] = 0
    dp[0][1] = arr[0] if K >= 1 else float('-inf')

    for i in range(1, N):
        for k in range(K + 1):
            # Option 1: skip arr[i]
            dp[i][k] = max(dp[i][k], dp[i-1][k])
            # Option 2: pick arr[i] if possible (need to ensure i >= 2 for non-adjacent)
            if k > 0:
                if i >= 2:
                    dp[i][k] = max(dp[i][k], dp[i-2][k-1] + arr[i])
                else:
                    dp[i][k] = max(dp[i][k], arr[i])
    
    # Return max value with at most K picks
    return max(dp[N-1][k] for k in range(K + 1))


n = int(input())
copy = n 
result = 0

while copy:
    result = result * 10 + copy % 10
    copy //= 10

if n == result:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")