def col_sum(mat):
    n = len(mat)        # number of rows
    m = len(mat[0])     # number of columns

    max_val = -1
    col_index = -1

    # Step 1: Find max element and its column index
    for i in range(n):
        for j in range(m):
            if mat[i][j] > max_val:
                max_val = mat[i][j]
                col_index = j

    # Step 2: Sum all elements in that column
    total = 0
    for i in range(n):
        total += mat[i][col_index]

    return total



class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def merge_trees(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1

    # Merge the two nodes
    new_node = Node(root1.val + root2.val)

    # Recursively merge the left and right children
    new_node.left = merge_trees(root1.left, root2.left)
    new_node.right = merge_trees(root1.right, root2.right)

    return new_node
