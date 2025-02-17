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