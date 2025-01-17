arr_len = int(input())
arr = list(map(int,input().split()))


prefix_sum = [0]*arr_len
for i in range(arr_len):
    if arr[i] % 3 == 0 :
        prefix_sum[i] = prefix_sum[i-1]+1
    else:
        prefix_sum[i] = prefix_sum[i-1]
# print(prefix_sum)

querry = int(input())
for i in range(querry):

    l,r = map(int,input().split())
    if l == 0:
        print(prefix_sum[r])
    else:
        print(prefix_sum[r]-prefix_sum[l-1])