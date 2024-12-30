array = [5,3,1,9,4]

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] <= arr[j+1]:
                pass
            elif arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
        
    return arr
print(bubbleSort(array))


def bubbleSort(x):
    for i in range(len(x)):
        for j in range(len(x)-i-1):
            if x[j] <= x[j+1]:
                pass
            elif x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
            
        
    return x
print(bubbleSort(array))