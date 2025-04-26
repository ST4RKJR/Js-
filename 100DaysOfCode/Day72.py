#Even Element Sum
def even_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        if arr[i] % 2 == 0 :
            result += arr[i]
    return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_leaf_similar(root1, root2):
    def get_leaves(root):
        leaves = []
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return leaves
    
    return 1 if get_leaves(root1) == get_leaves(root2) else 0
