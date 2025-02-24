def selection_sort(seq):
    # mini = seq[0]
    # for i in range(len(seq)):
    #     for j in range(i,len(seq)):
    #     if seq[i] < mini:
    #         mini = seq[i]
    # return mini
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1,len(seq)):
            if(seq[j] < seq[min_index]):
                min_index = j
        seq[i],seq[min_index] = seq[min_index],seq[i]
    return seq
    
    # for i in range(len(seq)):
    #     if seq[index] > mini(seq[1::]):
    #         seq[index] = mini(seq[1::])
    #         index += 1
    # return seq
