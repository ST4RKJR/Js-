#Minimum Size Subarray Sum K
def minSubArray(arr, k):
    l = len(arr)
    mini = float('inf')
    x = 0
    summ = 0

    for y in range(l):
        summ += arr[y]

        while summ >= k:
            mini = min(mini, y - x + 1)
            summ -= arr[x]
            x += 1

    if mini != float("inf"):
        return mini 
    else:
        return 0
    
#Prefix Removals
