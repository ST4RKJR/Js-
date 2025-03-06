#Container with most water
def maxAmount(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        max_area = max(max_area, (right - left) * min(height[left], height[right]))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
#Subarrays Sum Equals Zero
def subarray_exists(arr, n):
#Write your code here


    # def subArrayExists(self,arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    st = set(prefix)
    if (len(st) == len(prefix)):
        return False
    else:
        return True
    
#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        prefix = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
           prefix[i] = prefix[i-1] + arr[i-1]
        st = set(prefix)
        if (len(st) == len(prefix)):
            return False
        else:
            return True
