#Even Element Sum
def even_sum(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        if arr[i] % 2 == 0 :
            result += arr[i]
    return result