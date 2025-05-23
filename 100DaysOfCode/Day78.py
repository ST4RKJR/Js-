## SUM THE ODD
def odd_sum(arr):
    ans = 0
    for i, val in enumerate(arr):
        ans += val if i % 2 else 0
    return ans