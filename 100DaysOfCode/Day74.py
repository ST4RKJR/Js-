class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def sizeBinaryTree(root):
    if root is None:
        return 0
    return 1 + sizeBinaryTree(root.left) + sizeBinaryTree(root.right)

def maxDepthBinaryTree(root):
    if root is None:
        return 0
    return 1 + max(maxDepthBinaryTree(root.left), maxDepthBinaryTree(root.right))

def minBinaryTree(root):
    if root is None:
        return float('inf')  # So that empty branches are ignored
    return min(root.key, min(minBinaryTree(root.left), minBinaryTree(root.right)))


'''
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.key = val
        self.left = left
        self.right = right
'''
class Solution:
    def maxDepthBinaryTree(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepthBinaryTree(root.left), self.maxDepthBinaryTree(root.right))

    def minBinaryTree(self, root):
        if root is None:
            return float('inf')  # So that empty branches are ignored
        return min(root.key, self.minBinaryTree(root.left), self.minBinaryTree(root.right))

    def sizeBinaryTree(self, root):
        if root is None:
            return 0
        return 1 + self.sizeBinaryTree(root.left) + self.sizeBinaryTree(root.right)
    
    