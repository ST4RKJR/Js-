## SUM THE ODD
def odd_sum(arr):
    ans = 0
    for i, val in enumerate(arr):
        ans += val if i % 2 else 0
    return ans

## BEST TIME TO BUY AND SELL STOCK III
def maxProfit(prices):
    n = len(prices)
    # prefix = [0] * (n)
    # prefix[0] = prices[0]
    # for i in range(1, n):
    #     prefix[i] = min(prefix[i - 1], prices[i])
    
    # suffix = [0] * (n)
    # suffix[n - 1] = prices[n - 1]
    # for i in range(n - 2, -1, -1):
    #     suffix[i] = max(suffix[i + 1], prices[i])
    
    # ans = 0
    # for i in range(n):
    #     ans = max(ans, suffix[i] - prefix[i])
    # return ans


    mini = prices[0]
    ans = 0
    for i in prices:
        mini = min(mini, i)
        ans = max(ans, i - mini)
    return ans