def frogJump(n, height, k):
    def helper(i):
        if i == 0:
            return 0
        min_energy = float('inf')
        for j in range(1, k+1):
            if i - j >= 0:
                min_energy = min(min_energy, helper(i-j) + abs(height[i] - height[i-j]))
        return min_energy

    return helper(n-1)