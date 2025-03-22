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


class Solution:
    def minSpeedOnTime(self, dist, hour: float) -> int:

        # check if it's possible to reach the office on time with a given speed
        def can_reach_on_time(speed):
            total_time = sum( ((d + speed - 1) // speed) for d in dist[:-1]) + dist[-1] / speed
            return total_time <= hour

        # binary search to find the minimum speed
        left, right = 1, 10**7
        while left < right:
            mid = (left + right) // 2
            if can_reach_on_time(mid):
                right = mid
            else:
                left = mid + 1
        
        if can_reach_on_time(left):
            return left
        else:
            return -1

#Element appearing more than 25% in Sorted Array
import bisect

def find_special_integer(arr):
    n = len(arr)
    threshold = n // 4

    for i in [n // 4, n // 2, 3 * n // 4]:
        num = arr[i]
        left = bisect.bisect_left(arr, num)
        right = bisect.bisect_right(arr, num)
        
        if right - left > threshold:
            return num