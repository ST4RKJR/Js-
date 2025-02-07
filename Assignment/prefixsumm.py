array = [1,2,3,4,5,6]
prefix_sum = []

suffix_sum = []

for i in range(len(array)):
    if i == 0:
        prefix_sum.append(array[i])
    else:
        prefix_sum.append(array[i]+prefix_sum[i-1])
    # if i == 0:
    #     suffix_sum.append(sum(array))
    # else:
    suffix_sum.append(sum(array[i::]))
        
print(prefix_sum)
print(suffix_sum)
