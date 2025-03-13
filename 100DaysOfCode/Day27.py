#Min Cost Climbing Stairs
def minCostClimbingStairs(cost):
    cost.append(0)
        
    for i in range(len(cost) - 4, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
        
    return min(cost[0], cost[1])