def count_ways(arr):
    n = len(arr)
    dp = [-1] * n   # memoization

    def dfs(i):
        if i == n - 1:
            return 1  # reached last stone
        if dp[i] != -1:
            return dp[i]

        total = 0
        for step in range(1, arr[i] + 1):
            nxt = i + step
            if nxt < n:
                total += dfs(nxt)

        dp[i] = total
        return dp[i]

    return dfs(0)
