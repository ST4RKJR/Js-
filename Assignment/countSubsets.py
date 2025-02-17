def subsets(lis,curr,target):
    if target == 0 :
        return 1
    if curr == len(lis) :
        return 0 
    s1 = subsets(lis,curr+1,target - lis[curr])
    s2 = subsets(lis,curr+1,target)
    return s1+s2


n,k = map(int,input().split())
lis = list(map(int,input().split()))
ans =subsets(lis,0,k)
print(ans)
