#Implementing Bubble Sort
def bubbleSort(seq):
    n = len(seq)
    for j in range(n):
        for i in range(n-j-1):
            if seq[i] > seq[i+1]:
                seq[i],seq[i+1] = seq[i+1],seq[i]

    return seq

#Sum of Odd Length Subarrays
def sumOddLengthSubarrays(arr):
    a = 0;
    count = 0
    n = len(arr)
    for i in range(n):
        count = count-(i+1)//2+(n-i+1)//2
        a += count*arr[i]
    return a