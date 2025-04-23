#Maximum Subarray Sum With One Deletion
def max_sum(arr):
    n = len(arr)
    # Initialize arrays for DP
    dp_no_delete = [0] * n
    dp_one_delete = [0] * n

    dp_no_delete[0] = arr[0]
    dp_one_delete[0] = float('-inf')
    max_result = arr[0]

    for i in range(1, n):
        dp_no_delete[i] = max(dp_no_delete[i - 1] + arr[i], arr[i])
        dp_one_delete[i] = max(dp_no_delete[i - 1], dp_one_delete[i - 1] + arr[i])
        max_result = max(max_result, dp_no_delete[i], dp_one_delete[i])

    return max_result

#Parent Node

'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''

def parent_node(root, X):
    if not root or root.val == X:
        return -1  

    queue = [(root, -1)]  

    while queue:
        current, parent = queue.pop(0)  

        if current.val == X:
            return parent  

        if current.left:
            queue.append((current.left, current.val))
        if current.right:
            queue.append((current.right, current.val))

    return -1  


class Solution:
    def maximumSum(self, arr) -> int:       

        mx = n0 = n1 = -1                             
                                                        
        for i, num in enumerate(arr):                                                        
            n1 = max(n0,  n1 + num)                     
            n0 = max(num, n0 + num)                     
            mx = max(mx,  n1,   n0)                                    
        return mx