#Search a 2D sorted Matrix
def searchMatrix(mat, target):
    n, m = len(mat), len(mat[0])
    left, right = 0, n * m - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, m)
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

#Minimum Time to Repair Cars
def repairCars(ranks, cars):
    def canRepairInTime(time):
        count = 0
        for r in ranks:
            count += int((time // r) ** 0.5)
            if count >= cars:
                return True
        return False

    left, right = 1, min(ranks) * cars * cars
    while left < right:
        mid = (left + right) // 2
        if canRepairInTime(mid):
            right = mid
        else:
            left = mid + 1

    return left