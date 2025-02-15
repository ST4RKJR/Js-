#Kth largest element in an Array


#It will work for large time limit
# def findKthLargest(nums, k):
#     copy = nums
#     new = []
#     for i in range(k-1):
#         new.append(max(copy))
#         copy.remove(max(copy))
#     return max(copy)

#It will work in shorter time period
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]