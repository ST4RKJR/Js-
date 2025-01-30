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
    



    