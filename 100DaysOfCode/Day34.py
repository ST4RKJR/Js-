#First Bad Version
def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid  # Search in the left half
        else:
            left = mid + 1  # Search in the right half
    return left

