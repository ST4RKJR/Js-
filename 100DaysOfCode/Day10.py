#Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, y):

    for x in letters:
        if y < x:
            return(x)
    else:
        return(letters[0])
    
#Pivot Index
def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        if left_sum == total - left_sum - nums[i]:
            return(i)
        left_sum += nums[i]
    else:
        return(-1)