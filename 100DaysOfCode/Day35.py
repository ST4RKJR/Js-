#Arrange Coins
def arrangeCoins(x):
    rows_covered = 0
    while x >= rows_covered + 1:
        rows_covered += 1
        x -= 1
    return rows_covered

import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(-1+math.sqrt(1+8*n))//2