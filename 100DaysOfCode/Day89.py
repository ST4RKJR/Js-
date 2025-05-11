# KnapSack
def maxWeight(wt, val, W):
    def f(W, val, wt, n, memo):

        if n == 0 or W == 0:
            return 0
        if memo[n][W] != -1:
            return memo[n][W]

        pick = 0

        if wt[n - 1] <= W:
            pick = val[n - 1] + f(W - wt[n - 1], val, wt, n - 1, memo)

        notPick = f(W, val, wt, n - 1, memo)
        memo[n][W] = max(pick, notPick)
        return memo[n][W]

    n = len(val)
    memo = [[-1] * (W + 1) for _ in range(n + 1)]

    return f(W, val, wt, n, memo)
