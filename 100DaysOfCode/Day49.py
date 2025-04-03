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

