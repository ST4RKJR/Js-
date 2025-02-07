def count_valid(n,arr):
    total_sum = sum(arr)
    left_sum = 0
    count = 0
    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum >= right_sum:
            count+=1
        left_sum+= arr[i]
    return count

n = int(input())
arr = list(map(int, input().split()))

print(count_valid(n, arr))