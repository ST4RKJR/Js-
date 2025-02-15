array = [10,20,20,5,15]
target = 30
count = 0
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if i == len(array)-1:
            if array[i] == target:
                count += 1
        elif array[i] + array[j] == target:
            count += 1
print(count)
             