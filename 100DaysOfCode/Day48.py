#Maximum Product of Three numbers
def MaxPro(arr):
    arr.sort()
    return max(arr[-1]*arr[-2]*arr[-3],arr[0]*arr[1]*arr[-1])




#Merging Intervals
def merge(intervals):
    intervals.sort()
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged