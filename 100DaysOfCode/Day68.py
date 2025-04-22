def sum_of_squares(N):
    return sum(i**2 for i in range(1, N+1))

# Example usage:
N = int(input("Enter a positive integer: "))
print(f"The sum of squares from 1 to {N} is {sum_of_squares(N)}")



class Solution:
    def preorderTraversal(self, root) -> list[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit root
            dfs(node.left)           # Traverse left subtree
            dfs(node.right)          # Traverse right subtree
        
        dfs(root)
        return result