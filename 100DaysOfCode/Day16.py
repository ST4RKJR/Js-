#Range Frequency Querry 
def numOfFreq(arr, queries):
    result = []
    for i, j, x in queries:
        result.append(arr[i:j+1].count(x))
    return result

#First and Last Position of Key in array
def searchRange(nums, target):
    def find_bound(is_first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound
    
    return [find_bound(True), find_bound(False)]