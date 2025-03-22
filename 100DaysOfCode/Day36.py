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