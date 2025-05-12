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


## ALTERNATE ELEMENTS
n = int(input())
arr = [int(i) for i in input().split()]


# for i in range(n):
#     if i % 2 == 0:
#         print(arr[i], end = " ")

# for i in range(0, n, 2):
#     print(arr[i], end = " ")

print(*arr[::2])