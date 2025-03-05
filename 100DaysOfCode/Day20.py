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
