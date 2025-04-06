Q = int(input())
for _ in range(Q):
    l1, r1, l2, r2, X = map(int, input().split())
    n = l2 - l1 + 1  # number of diagonal steps
    sum_val = 0
    i = l1
    j = r1

    for k in range(n):
        val = (i + k)**2 + (j + k)**2
        if val % X == 0:
            sum_val += val
    print(sum_val)
    
    
#palindrome check 
