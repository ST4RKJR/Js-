from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_sum = 0
        level_count = len(queue)

        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_count)

    return result


def max_treasure(n, k, treasure):
    dp = [0] * n

    for i in range(n):
        take = treasure[i]
        if i - k - 1 >= 0:
            take += dp[i - k - 1]
        skip = dp[i - 1] if i > 0 else 0
        dp[i] = max(skip, take)

    return dp[n - 1]
