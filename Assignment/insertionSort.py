array = [1,2,9,1,2,5]
index = [0,1,2,3,4,5]

def insertionSort(x):
    n = len(x)
    
    for i in range(1,n):
        key = x[i]
        j = i - 1
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -= 1
        
        print('x',x)
        x[j+1] = key
        print(j,x)
        
    return x

print(insertionSort(array))
 
        
        