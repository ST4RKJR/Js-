#Maximum Product of Three numbers
def MaxPro(arr):
    arr.sort()
    return max(arr[-1]*arr[-2]*arr[-3],arr[0]*arr[1]*arr[-1])

class Solution:
    def maximumProduct(self, nums) -> int:
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        for num in nums:
            if num > max1:
                max1, max2, max3 = num, max1, max2
            elif num > max2:
                max2, max3 =num, max2
            elif num > max3:
                max3 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, min1 * min2 * max1)
                        


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

class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x [0])

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        return ans