#Sub arrays Divisivle by K
N, K = map(int, input().split())
A = list(map(int, input().split()))
map = {0: 1}
prefix_sum = 0
count = 0
for num in A:
    prefix_sum += num
    remainder = prefix_sum % K
    if remainder < 0:
        remainder += K
    if remainder in map:
        count += map[remainder]
        map[remainder] += 1
    else:
        map[remainder] = 1
print(count)

