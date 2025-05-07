from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def max_spread(root):
    if not root:
        return 0

    max_width = 0
    # Queue stores (node, index)
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        _, first_index = queue[0]
        for i in range(level_size):
            node, index = queue.popleft()
            if node.left:
                queue.append((node.left, 2 * index))
            if node.right:
                queue.append((node.right, 2 * index + 1))
        _, last_index = node, index  # `node` and `index` from last loop iteration
        max_width = max(max_width, last_index - first_index + 1)

    return max_width

