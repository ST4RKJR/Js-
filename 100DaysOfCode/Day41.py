#Nth Tribonacci 





#Frog Jump with K Distance (DP)
D = {}
def frogJump(n, height, k):
    def solve(i):
        if i == n - 1:
            return 0
        if i in D:
            return D[i]
        min_jump = float('inf')
        for j in range(1, min(k,n -i)+1):
            if i +j< n:
                cost = abs(height[i] -height[i+j]) + solve(i+j)
                min_jump = min(min_jump,cost)
        D[i] = min_jump
        return min_jump
    return solve(0)