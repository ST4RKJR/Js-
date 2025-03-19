#First Bad Version
def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left<right:
            mid = (left+right)//2
            

#Diagonal Binary Search
def searchMatrix(matrix, target):
    n = len(matrix)
    row, col = 0, n - 1

    while row < n and col >= 0:
        if matrix[row][col] == target:
            print(True)
            return
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    print(False)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
target = int(input())

searchMatrix(matrix, target)