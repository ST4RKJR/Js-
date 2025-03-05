#Factorial using Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

n = int(input())
print(factorial(n))

#Subsequence
from itertools import combinations

s = input().strip()
subsequences = sorted("".join(comb) for r in range(1, len(s) + 1) for comb in combinations(s, r))
print(" ".join(subsequences))