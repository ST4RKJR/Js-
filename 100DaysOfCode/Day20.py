#Capacity To Ship Packages Within D Days
def shipWithinDays(weights, D):
    def canShip(capacity):
        days = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                days += 1
                current_load = 0
            current_load += w
        return days <= D

    left, right = max(weights), sum(weights)
    while left < right:
        mid = (left + right) // 2
        if canShip(mid):
            right = mid
        else:
            left = mid + 1
    return left

#Quadratic Equation Quest 
import math

def findX(K):
    a, b, c = 2, 5, -K
    D = b * b - 4 * a * c  # Discriminant

    if D < 0:
        print(-1)
        return
    
    sqrt_D = math.isqrt(D)
    if sqrt_D * sqrt_D != D:  # Check if D is a perfect square
        print(-1)
        return
    
    x1 = (-b + sqrt_D) // (2 * a)
    x2 = (-b - sqrt_D) // (2 * a)
    
    if x1 > 0 and (2 * x1 * x1 + 5 * x1 == K):
        print(x1)
    elif x2 > 0 and (2 * x2 * x2 + 5 * x2 == K):
        print(x2)
    else:
        print(-1)

# Input
K = int(input())
findX(K)