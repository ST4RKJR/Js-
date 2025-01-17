arr_len = int(input())
arr = list(map(int,input().split()))
target = int(input())

# for i in range(arr_len):
#     if arr[i] == target:
#         print(i)
#     else:
#         if arr[i] > target:
#             print(i)
#             break

def find_insert(arr_len,arr,target):
    for i in range(arr_len):
        if target > arr[-1]:
            return(arr_len)
        if arr[i] == target:
            return(i)
        else:
            if arr[i] > target:
                return(i)
            # elif target > arr_len:
            #     return(arr_len)

print(find_insert(arr_len,arr,target))