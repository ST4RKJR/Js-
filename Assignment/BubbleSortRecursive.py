def recursive_bubble(seq, n=None, i=0):
    if n is None:
        n = len(seq)
    
    if n == 1:
        return
    
    if i < n - 1:
        if seq[i] > seq[i + 1]:
            seq[i], seq[i + 1] = seq[i + 1], seq[i]
        recursive_bubble(seq, n, i + 1)
    else:
        recursive_bubble(seq, n - 1, 0)

T = 2
test_cases = [
    ([4, 1, 3, 9, 7], 5),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10)
]

for seq, n in test_cases:
    recursive_bubble(seq, n)
    print(seq)
    
    
    