n,q = map(int,input().split())
a = list(map(int,input().split()))
p = [a[0]]
for i in range(1,n):
    p.append(p[i-1]^a[i])
for _ in range(q):
    l,r = map(int,input().split())
    if l==0:
        print(p[r])
    else:
        print(p[r]^p[l-1])