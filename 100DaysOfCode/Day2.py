#Maximum Score After Splitting a String
def maxScore(s):
    s = list(s)
    zerocunt = 0
    onecount = s.count('1')
    maxi = 0
    for i in range(len(s)-1):
        if s[i]=="0":
            zerocunt+=1
        if s[i]=="1":
            onecount-=1
        maxi = max(maxi,onecount+zerocunt)
    return(maxi)


#100 Days of Code Completed?
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
valid=True
for i in range(100):
    if arr1[i]==1 or arr2[i]==1:
        pass
    else:
        valid=False
        break
print(valid)