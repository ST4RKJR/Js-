def bubble_sort_ascending(array):
    for j in range(len(array)):
        swapCheck = False
        for i in range(len(array)-j-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swapCheck = True
        if swapCheck == False:
            break
    return array
                        
array = [2,1,9,3,8]
print(bubble_sort_ascending(array))