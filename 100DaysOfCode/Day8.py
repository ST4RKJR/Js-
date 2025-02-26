#Running Sum of 1D Array
def runningSum(nums):
    n = len(nums)
    prefix=[]
    for i in range(n):
        if i == 0:
            prefix.append(nums[i])
        else:
            prefix.append(nums[i]+prefix[i-1])
    return prefix

