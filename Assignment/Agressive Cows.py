def helper(k,arr,cow):
    lst = arr[0]

    cow-=1
    for i in range(1,len(arr)):
        if(abs(arr[i]-lst) >= k):
            lst = arr[i]
            cow -=1 
    return cow<=0



def solve(n, k, stalls):
    l = 0
    r= 10**9
    stalls.sort()
    while(r-l+1>2):
        mid = l + (r-l)//2
        if(helper(mid,stalls,k)):
            l = mid 
        else:
            r = mid 
    return l