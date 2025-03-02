#Sort Colors
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums


#Inversion in bubble sort
def count_inversions(list_of_numbers):
    count = 0
    n = len(list_of_numbers)
    for i in range(n):
        for j in range(n - 1 - i):
            if list_of_numbers[j] > list_of_numbers[j + 1]:
                list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]
                count += 1
    return count