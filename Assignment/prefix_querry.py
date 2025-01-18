N,Q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(Q):
    l,r = map(int,input().split())
    p = [arr[l]]
    for i in range(l,r+1):
        p.append(p[i-l]&arr[i])
    print(p[-1])