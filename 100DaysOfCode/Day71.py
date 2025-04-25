#Even Odd Difference
n = int(input())
arr = list(map(int,input().split()))
even = 0
odd = 0
for i in range(n):
    if i % 2 == 0 :
        even += arr[i]
    else:
        odd += arr[i]
print(even-odd)


#
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(level_order):
    if not level_order or level_order[0] == -1:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1
    n = len(level_order)

    while queue and i < n:
        current = queue.pop(0)

        # Left child
        if i < n and level_order[i] != -1:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < n and level_order[i] != -1:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root
