# s = input()
# c = input()
# ans = -1
# # rev = []
# # for j in s:
# #     rev.append(j)
# # rev.sort()


# # for i in range(len(s)-1,-1,-1):
# #     if s[i] == c:
# #         ans = i
# #         break
# # print(ans)

# # maxi = 0
# # for i in range(len(s)):
# #     if s[i] == c:
# #         maxi = i 
        
# # if maxi == 0:
# #     print(-1)
# # else:
# #     print(maxi)
    
    
# maxi = -1
# for i in range(len(s)):
#     if s[i] == c:
#         maxi = i 
        
# print(maxi)
nums = [10, 20, 30, 40, 50]
print(nums)
nums[1], nums[3] = nums[3], nums[1]
print(nums)


#BINARY SEARCH FOR INCREASING ORDER ARRAY


# arr = [1,2,3,4,5,6,7,8,9,10]

# def binary_search(arr,target):
    
#     left = 0
#     right = len(arr)
#     while (left <= right):
#         mid = (left + right)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "Not Found"

# target = int(input())
# print(binary_search(arr,target))



# BINARY SEARCH FOR DECREASING ARRAY


array = [9,8,7,6,5,4,3,2,1]

def binary_search(array,x):
    
    left = 0
    right = len(array)
    while (left <= right):
        mid = left + (right-left)//2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"

x = int(input())
print(binary_search(array,x))


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