def range_sum(lst, L, R):
    return sum(lst[L:R+1])


lst = list(map(int, input().split()))
L, R = map(int, input().split())

print(range_sum(lst, L, R))