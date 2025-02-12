N, P = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
ans = 0
start = 0
end = 1
while start < N-1:
    while end <N and (l[end]-l[start]<=P):
        end +=1
    b = end-start -1
    if b >0:
        ans +=b*(b -1) // 2
    start += 1
print(ans)