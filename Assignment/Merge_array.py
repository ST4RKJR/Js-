a = list(map(int,input().split())).sort()
b = list(map(int,input().split())).sort()
c = a+b
def merge_array(arr,l ,r ):
    if l >= r-1:
        return arr
    mid = (l+r)//2
    return max((arr,l,mid),max(arr,mid,r))

print(merge_array(c,0,len(c)))