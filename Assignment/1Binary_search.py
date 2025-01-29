# def binary_search(arr,target):
#     left = 0
#     right = len(arr)-1
#     ans = 0
#     while left <= right:
#         mid = (left + right)//2 
#         if arr[mid] < target:
#             left += 1
#         elif arr[mid] > target:
#             right -= 1
#         else:
#             ans = mid
#             right = mid - 1
#     return(ans)
                
            
# array = [11, 22, 33 , 44 , 44 , 55 , 66 , 77]          
# target = 44
# print(binary_search(array,target))

# def binary_search(array, target):
#     left = 0 
#     right = len(array)-1
#     while left <= right:
        
# find square root of a number 
x = 35
idx = 1
while idx**2 <= x:
    idx += 1
if idx**2 == x:
    print(idx)
else:
    print(idx - 1)
    
target = 35
low = 1
high = target
