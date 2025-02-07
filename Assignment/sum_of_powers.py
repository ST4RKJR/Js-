# def sumPowers(n, x):
#     if x == 0:
#         return 1
#     return n ** x + sumPowers(n,x-1)

# n = 5
# x = 4
# print(sumPowers(n,x))


# # f(n,x) = n0 + n1 + n2 + ..... + n^x
# #        = n0 + n(n0 + n1 + ....... + n^x-1)

def find_val(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    else:
        return max(arr[index], find_val(arr, index + 1))
    
arr = [5,3,8,1]
index = 0
print(find_val(arr,index))