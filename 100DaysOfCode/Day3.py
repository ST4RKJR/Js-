
# #Minimum Value to Get Positive Step by Step Sum
# def minStartValue(nums):
#     prefix_sum = 0
#     min_start_value = 1
        
#     for num in nums:
#         prefix_sum += num
#         min_start_value = max(min_start_value, 1 - prefix_sum)
        
#     return min_start_value

# #Favorite Sequence
# import math
# t=int(input())
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     l=[]
#     for i in range(math.ceil(n/2)):
#         if i!=(n-1-i):
#             l.extend([arr[i],arr[n-1-i]])
#         else:
#             l.append(arr[i])
#     print(*l)

arr = [5, 3, 4, 1]
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)