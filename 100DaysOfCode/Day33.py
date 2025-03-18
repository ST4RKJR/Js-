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
