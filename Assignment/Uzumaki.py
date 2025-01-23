count1 = 1
count2 = 2
for i in range(8): 
    for j in range(3):  
        k = i
        while k > 0:  
            count1 += 1
            k //=2
        count2 += 2
print(count1, count2)
