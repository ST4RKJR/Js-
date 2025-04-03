#Insert Interval
def insert(intervals, newInterval):
    res = []
    i = 0
    n = len(intervals)

    # Add all intervals before the new interval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    # Add remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res
    
    
#Jump Game (Memoization)
def canJump():
    n = int(input())
    nums = list(map(int, input().split()))
    
    maxReach = 0
    for i in range(n):
        if i > maxReach:
            print("false")
            return
        maxReach = max(maxReach, i + nums[i])
    
    print("true")

canJump()