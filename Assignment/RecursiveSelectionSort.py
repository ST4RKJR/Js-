def selection_sort_recursive(seq, i=0):
    if i >= len(seq) - 1:
        return seq
    min_index = i
    for j in range(i + 1, len(seq)):
        if seq[j] < seq[min_index]:
            min_index = j
    seq[i], seq[min_index] = seq[min_index], seq[i]
    return selection_sort_recursive(seq, i + 1)

seq = [4,3,2,8,1]
print(selection_sort_recursive(seq))