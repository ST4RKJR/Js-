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


## SUM OF EVEN 

class Node:
    def __init__(self, val=1):
        self.val = val
        self.left = None
        self.right = None


from collections import deque

def build_tree(level_order):
    if not level_order or level_order[0] == 0:
        return None

    root = Node(level_order[0])
    queue = deque([root])
    i = 1

    while queue and i < len(level_order):
        current = queue.popleft()
        
        # Left child
        if i < len(level_order) and level_order[i] != 0:
            current.left = Node(level_order[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(level_order) and level_order[i] != 0:
            current.right = Node(level_order[i])
            queue.append(current.right)
        i += 1

    return root