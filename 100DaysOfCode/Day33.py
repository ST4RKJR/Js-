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