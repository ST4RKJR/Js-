#Profit Max
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit


class Solution:
    def maxProfit(self, prices) -> int:
        min_price = prices[0]
        max_profit = 0
        for cost in range(1, len(prices)):
            max_profit = max(max_profit, prices[cost]-min_price)
            min_price = min(min_price, prices[cost])
        return max_profit