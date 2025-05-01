'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def count_occurrences(head, K):
    count = 0
    current = head
    while current:
        if current.data == K:
            count += 1
        current = current.next
    return count

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_unival_tree(root):
    def dfs(node, value):
        if node is None:
            return True
        if node.val != value:
            return False
        return dfs(node.left, value) and dfs(node.right, value)

    return dfs(root, root.val)
