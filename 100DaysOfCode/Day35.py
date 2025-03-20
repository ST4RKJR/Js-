#Arrange Coins
def arrangeCoins(x):
    rows_covered = 0
    while x >= rows_covered + 1:
        rows_covered += 1
        x -= 1
    return rows_covered

import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-1+math.sqrt(1+8*n))//2
    
#Find Peak Element
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

class Solution:
    def findPeakElement(self, nums) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l