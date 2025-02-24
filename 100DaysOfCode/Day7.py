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

#Little Alice and Numbers
N = int(input())
arr = list(map(int, input().split()))
Q = int(input())
prefix = [0] * (N + 1)

for i in range(N):
    prefix[i + 1] = prefix[i] + (arr[i] % 5 == 0)

for _ in range(Q):
    l, r = map(int, input().split())
    print(prefix[r + 1] - prefix[l])