#Parity Sum Difference Querry
def parity_queries(arr, queries):
    n = len(arr)
    prefix_even = [0] * (n + 1)
    prefix_odd = [0] * (n + 1)
    
    for i in range(1, n+1):
        num = arr[i-1]
        if num % 2 == 0:
            prefix_even[i] = prefix_even[i-1] + num
            prefix_odd[i] = prefix_odd[i-1]
        else:
            prefix_even[i] = prefix_even[i-1]
            prefix_odd[i] = prefix_odd[i-1] + num
    
    results = []
    for query in queries:
        L, R = query
        sum_even = prefix_even[R+1] - prefix_even[L]
        sum_odd = prefix_odd[R+1] - prefix_odd[L]
        results.append(sum_even - sum_odd)
    
    return results