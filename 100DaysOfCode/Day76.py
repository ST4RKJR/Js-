from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def right_view(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # If it's the last node in this level, add it to the result
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def internal_nodes(root):
    if not root:
        return 0

    # A node is internal if it has at least one child
    left_count = internal_nodes(root.left)
    right_count = internal_nodes(root.right)
    
    if root.left or root.right:
        return 1 + left_count + right_count
    else:
        return 0  # It's a leaf node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):
        queue = deque()
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        result = []
        queue.append(root)
        while queue:
            child_queue = deque()
            prev = -1
            while queue:
                curr = queue.popleft()

                if curr.left is not None:
                    child_queue.append(curr.left)

                if curr.right is not None:
                    child_queue.append(curr.right)
                
                prev = curr
            
            result.append(prev.val)
            queue = child_queue
        
        return result