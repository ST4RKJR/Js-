# def book_allocation(arr,n,m):
    
    
    
    
    
    
#    return m 
    
    
    
    
def check(arr,K,load):
    min_arr = max(arr)
    max_arr = sum(arr)
    while min_arr <= max_arr:
        
    
    
    
arr = [12,34,67,90,54,5]
n = 4 #books
m = 2 #students


def solver(arr,k,m):
    tot = 0
    for i in range(len(arr)):
        tot += arr[i]
        if(tot > k):
            m -= 1
            tot = arr[i]
            if(tot > k):
                return False
    m-=1
    return m>=0 and tot<=k


def book_allocation(arr, n, m):
    l = 0
    r = sum(arr)
    if(n<m):
        return -1

    
    while(r-l+1 > 2):
        mid = l + (r-l)//2
        if(solver(arr,mid,m)):
            r = mid 
        else:
            l = mid 
    return r





