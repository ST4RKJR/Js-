def bubble_sort_descending(array):
    for i in range(len(array)):
        swap = False
        for j in range(len(array)-i-1):
            if array[j] < array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swap = True
        if swap == False :
            break
    return array

array = [1,2,3,4,5]
print(bubble_sort_descending(array))