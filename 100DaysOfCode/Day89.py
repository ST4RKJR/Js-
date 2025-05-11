# KnapSack
def maxWeight(wt, val, W):
    def f(W, val, wt, n, memo):

        if n == 0 or W == 0:
            return 0
        if memo[n][W] != -1:
            return memo[n][W]

        pick = 0

        if wt[n - 1] <= W:
            pick = val[n - 1] + f(W - wt[n - 1], val, wt, n - 1, memo)

        notPick = f(W, val, wt, n - 1, memo)
        memo[n][W] = max(pick, notPick)
        return memo[n][W]

    n = len(val)
    memo = [[-1] * (W + 1) for _ in range(n + 1)]

    return f(W, val, wt, n, memo)


# Merge Sorted Array 
def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1 
    right = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[right] = nums1[i]
            i -= 1
        else:
            nums1[right] = nums2[j]
            j -= 1

        right -= 1