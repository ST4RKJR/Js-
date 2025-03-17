#Find Subsets 
from itertools import chain, combinations

def findSubsets(nums):
    return [list(subset) for subset in chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))]

#Count Subsets with Sum K- Recursion
def countSubsets(nums, n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if nums[n - 1] > k:
        return countSubsets(nums, n - 1, k)
    return countSubsets(nums, n - 1, k) + countSubsets(nums, n - 1, k - nums[n - 1])

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(countSubsets(nums, n, k))