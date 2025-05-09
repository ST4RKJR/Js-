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

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_nodes = []

        for _ in range(level_size):
            node = q.popleft()
            level_nodes.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_nodes)

    return result
