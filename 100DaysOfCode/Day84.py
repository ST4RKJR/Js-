'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def invert_binary_tree(root):
    if root is None:
        return None
    
    # Swap the children
    root.left, root.right = root.right, root.left
    
    # Recur on left and right subtrees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    
    return root
