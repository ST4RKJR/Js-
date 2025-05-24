## COIN CHANGE
def coin_change_minimum():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        amount = int(data[index])
        index += 1
        n = int(data[index])
        index += 1
        coins = list(map(int, data[index:index + n]))
        index += n
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        if dp[amount] == float('inf'):
            results.append("Not Possible")
        else:
            results.append(str(dp[amount]))
    
    print('\n'.join(results))

coin_change_minimum()