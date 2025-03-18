#Find The Element
def isPresent(arr, X):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == X:
            return True
        elif arr[mid] < X:
            left = mid + 1
        else:
            right = mid - 1
    return False
class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1

#Find Closest Number in Sorted Array
def findClosest(arr, K):
    left, right = 0, len(arr) - 1
    closest = arr[0]
    
    while left <= right:
        mid = (left + right) // 2
        
        if abs(arr[mid] - K) < abs(closest - K) or (abs(arr[mid] - K) == abs(closest - K) and arr[mid] > closest):
            closest = arr[mid]
        
        if arr[mid] < K:
            left = mid + 1
        else:
            right = mid - 1
    
    return closest



from typing import List


class Solution:
    def findClosest(self, arr, k):
        # code here
        possible1=0
        possible2=0
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if abs(arr[mid]-k)==0:
                return arr[mid]
            elif arr[mid]>k:
                possible1=mid
                right=mid-1
            else:
                possible2=mid
                left=mid+1
        if abs(arr[possible1]-k)<abs(arr[possible2]-k):
            return arr[possible1]
        elif abs(arr[possible1]-k)==abs(arr[possible2]-k):
            return arr[possible1]
        return arr[possible2]

