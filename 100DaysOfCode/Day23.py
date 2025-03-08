#Magical Array
def magicalArrays(arr):
    n = len(arr)
    count = 0
    i = 0

    while i < n:
        j = i
        while j < n and arr[j] == arr[i]:
            j += 1
        length = j - i
        count += (length * (length + 1)) // 2
        i = j

    return count

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        res = []
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        for i in range(len(nums)-1):
            res.append(nums[i+1]-nums[i])
        return max(res)
