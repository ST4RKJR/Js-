arr = [9,1,4,2,3,0]

for i in range(1,len(arr)):
    key = arr[i] 
    ind = i - 1
    while ind >= 0 and key < arr[ind]:
        arr[ind+1]= arr[ind]
        ind -= 1
    arr[ind+1] = key
           
print(arr)
    
    