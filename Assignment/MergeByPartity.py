def merge_sorted(arr1, arr2):
    i, j, merged = 0, 0, []
    
    while i < len(arr1) or j < len(arr2):
        if j == len(arr2) or (i < len(arr1) and arr1[i] <= arr2[j]):
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    return merged

n, m = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

merged = merge_sorted(arr, brr)

even = []
odd = []
for num in merged:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print(*even, *odd)