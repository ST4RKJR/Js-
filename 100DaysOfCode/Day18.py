#Implementing insertion sort
def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = key
    return seq


class Solution:
    def sortArray(self, lst: List[int]) -> List[int]:
        def heapify(heap_size, index):
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < heap_size and lst[left] > lst[largest]:
                largest = left
            if right < heap_size and lst[right] > lst[largest]:
                largest = right
            if largest != index:
                lst[index], lst[largest] = lst[largest], lst[index]
                heapify(heap_size, largest)
         
        for i in range(len(lst) //2-1, -1, -1):
            heapify(len(lst), i)
            
        for i in range(len(lst)-1, 0, -1):
            lst[i], lst[0] = lst[0], lst[i]
            heapify(i,0)
            
        return lst
        
        
#Inversion bubble sort - Hard 
def count_inversions(list_of_numbers):
    n = len(list_of_numbers)
    inversions = 0
    for j in range(n):
        swapCheck = False
        for i in range(n-j-1):
            if list_of_numbers[i] > list_of_numbers[i+1]:
                list_of_numbers[i],list_of_numbers[i+1] = list_of_numbers[i+1],list_of_numbers[i]
                swapCheck = True
                inversions += 1
        if swapCheck == False:
            break
    return inversions