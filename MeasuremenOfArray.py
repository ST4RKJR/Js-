#Sort the given array 
#calculate the sanity of an element in the array  which is defined as the sum of the original index (before sorting ) and the index of the last occurence of the new array(after sorting)

arr = [2,1,3,2,3,1]
#srt= [1,1,2,2,3,3]
sortedarr = sorted(arr)
ans = 0
for i in range(len(arr)):
    for j in range(len(sortedarr)-1,-1,-1):
        # print(j)
        if arr[i] == sortedarr[j]:
            ans += (j + i)
            break
        
print(ans)
        