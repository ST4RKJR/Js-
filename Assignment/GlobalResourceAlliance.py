n=int(input())
v=list(map(int,input().split()))
deno=(n*(n-1))/2
ct=0
for i in range(len(v)):
    for j in range(i,len(v)):
        if(v[j]<v[i]): ct+=1;
print(round(ct/deno,6))