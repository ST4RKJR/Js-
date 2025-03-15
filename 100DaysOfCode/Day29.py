#Kth Symbol in Grammar
def kthGrammar(n, k):
    if n == 1:
        return 0
    parent = kthGrammar(n - 1, (k + 1) // 2)
    return parent if k % 2 == 1 else 1 - parent

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        length = 2 ** (n - 2)
        if k <= length:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - length)
        
# Frog Jump with k Distances (Recursion)
def frogJump(n, height, k):
    def recur(idx):
        if idx == 0:
            return 0
        min_energy = float('inf')
        for j in range(1, min(k, idx) + 1):
            min_energy = min(min_energy, recur(idx - j) + abs(height[idx] - height[idx - j]))
        return min_energy

    return recur(n - 1)