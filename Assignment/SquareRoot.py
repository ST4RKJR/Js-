def sqrt(n):
    l, r = 0, n
    while l <= r:
        m = (l + r) // 2
        sq_m = m * m 
        if sq_m == n:
            return m 
        elif sq_m > n:
            r = m - 1
        else:
            l = m + 1
    return r 
for _ in range(int(input())):
    n = int(input())
    print(sqrt(n))