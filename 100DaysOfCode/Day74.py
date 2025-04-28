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
