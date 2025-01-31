# # def searchMatrix(mat,target):
# #     for i in range(n):
# #         if mat[i][0] <= target or mat[i][m-1] >= target:
# #             for j in range(m):
# #                 if mat[i][j] == target:
# #                     return True
# #             return False
                
                
# # mat = [[1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19]]
# target = [11]
# n , m = 5,5
# # print(searchMatrix(mat,target))


# def searchMatrix(mat, target):
#         for i in range(m):
#             mid = 0
#             k = -1
#             left = 0
#             right = len(mat[i])-1
#             while (left <= right):
#                 mid = (right+left)//2
#                 if mat[i][mid] == target:
#                     k = 1
#                     break
#                 elif mat[i][mid] < target:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             if k == 1: 
#                 return True
#         return False
    



    

# def binary_search_on_row(mat,target,row):
#     M = len(mat[0])
#     left = 0 
#     right = M - 1
#     while left <= right:
#         middle = (left+ right)//2
#         if mat[row][middle] == target:
#             return True
#         elif mat[row][middle] > target:
#             right = middle - 1
#         else:
#             left = middle + 1

# def binary_search(mat,target):         

#     N, M = len(mat) ,len(mat[0])
#     low  = 0 
#     high = N - 1


#     while low <= high:
#         mid = (low+high)//2
#         if mat[mid][0] <= target <= mat[mid][M-1]:
#             return binary_search_on_row(mat,target,mid)
            
#         elif mat[mid][M-1] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
            
            
# #Row traversal = 5 * row

# def searchMatrix(mat,target):
#     lo = 0 
#     n = len(mat)
#     m = len(mat[0])
#     hi = m*n-1
    
#     while lo <= hi :
#         mid = (lo+hi)//2
#         row = mid//m
#         col = mid % m
#         if mat[row][col]== target :
#             return True
#         elif mat[row][col] > target :
#              hi = mid - 1
#         else:
#             lo = mid + 1
#     return False


# def function(arr):
#     for i in arr:
#         if arr.count(i) == 1:
#             return i

# arr = [4, 3, 4, 5, 5]
# print(function(arr))

# def my_function(words):
#     seen = set()
#     for word in words:
#         if word in seen:
#             return word
#         seen.add(word)

# words = ["apple", "banana", "cherry", "apple", "date"]
# print(my_function(words))

def my_code(arr, x):
    left, right = 0, len(arr) - 1
    closest = arr[0]
    while left <= right:
        mid = (left + right) // 2
        if abs(arr[mid] - x) < abs(closest - x):
            closest = arr[mid]
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return closest

arr = [1, 2, 8, 10, 10, 12, 19]
x = 6
print(my_code(arr, x))

def function1(arr, t):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            result = mid
            right = mid - 1  # Move left to find the first occurrence
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return result
    
def function2(arr, t):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == t:
            result = mid
            left = mid + 1  # Move right to find the last occurrence
        elif arr[mid] < t:
            left = mid + 1
        else:
            right = mid - 1
    return result

def my_func(arr, t):
    first = function1(arr, t)
    if first == -1:
        return 0
    last = function2(arr, t)
    return last - first + 1

arr = [1, 2, 2, 3, 3, 5, 5, 5, 6]
t = 5
print(my_func(arr, t))