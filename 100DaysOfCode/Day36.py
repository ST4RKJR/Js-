#minimum speed to arrive on time
import math

def min_speed(dist, hour):
    left, right = 1, 10**5
    res = -1

    while left <= right:
        mid = (left + right) // 2
        time = sum(math.ceil(d / mid) for d in dist[:-1]) + dist[-1] / mid
        
        if time <= hour:
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res