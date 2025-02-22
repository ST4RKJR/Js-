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

array = [5,8, 1, 3, 2, 4]
print(count_inversions(array))