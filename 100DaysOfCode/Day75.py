def even_sum(arr):
    return sum(arr[i] for i in range(0, len(arr), 2))

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level_size = len(queue)
        level_nodes = []

        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Reverse the level if not left-to-right
        if not left_to_right:
            level_nodes.reverse()

        result.append(level_nodes)
        left_to_right = not left_to_right

    return result

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        q=[]
        if not root:
            return []
        q.append(root)
        res=[]
        flip=True
        while q:
            res.append([])
            level=[]
            while q:
                node=q.pop()
                res[-1].append(node.val)
                if flip:
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
                else:
                    if node.right:
                        level.append(node.right)
                    if node.left:
                        level.append(node.left)
            q=level
            flip=not flip
        return res