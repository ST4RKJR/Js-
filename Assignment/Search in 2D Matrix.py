# def searchMatrix(mat,target):
#     for i in range(n):
#         if mat[i][0] <= target or mat[i][m-1] >= target:
#             for j in range(m):
#                 if mat[i][j] == target:
#                     return True
#             return False
                
                
# mat = [[1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]
target = [11]
n , m = 5,5
# print(searchMatrix(mat,target))


def searchMatrix(mat, target):
        for i in range(m):
            mid = 0
            k = -1
            left = 0
            right = len(mat[i])-1
            while (left <= right):
                mid = (right+left)//2
                if mat[i][mid] == target:
                    k = 1
                    break
                elif mat[i][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if k == 1: 
                return True
        return False
    



    

def binary_search_on_row(mat,target,row):
    M = len(mat[0])
    left = 0 
    right = M - 1
    while left <= right:
        middle = (left+ right)//2
        if mat[row][middle] == target:
            return True
        elif mat[row][middle] > target:
            right = middle - 1
        else:
            left = middle + 1

def binary_search(mat,target):         

    N, M = len(mat) ,len(mat[0])
    low  = 0 
    high = N - 1


    while low <= high:
        mid = (low+high)//2
        if mat[mid][0] <= target <= mat[mid][M-1]:
            return binary_search_on_row(mat,target,mid)
            
        elif mat[mid][M-1] < target:
            low = mid + 1
        else:
            high = mid - 1