def rangeSum(L, R):
    if L==R+1:
        return 0
    return L+rangeSum(L+1,R)