# minimum absolute difference in BST

'''
class Node:
    def __init__(self, val=1):
        self.val = val
        self.left = None
        self.right = None
'''

def min_diff(root):
    ans = float("inf")
    prev = None
    def dfs(root):
        nonlocal ans, prev
        if not root:
            return 
        
        dfs(root.left)

        ans = min(ans, root.val - prev) if prev else ans
        prev = root.val 

        dfs(root.right)
    
    dfs(root)

    return 