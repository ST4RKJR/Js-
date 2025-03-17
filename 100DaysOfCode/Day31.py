#Find Subsets 
from itertools import chain, combinations

def findSubsets(nums):
    return [list(subset) for subset in chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))]

