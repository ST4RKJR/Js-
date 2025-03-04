#Koko eating bananas
def minEatingSpeed(piles, h):
    left, right = 1, max(piles)
    
    while left < right:
        mid = (left + right) // 2
        hours = sum((pile + mid - 1) // mid for pile in piles)
        
        if hours > h:
            left = mid + 1
        else:
            right = mid
    
    return left

#Square Root Of an Integer
# Your code here
def floor_sqrt(n):
    if n == 0 or n == 1:
        return n
    left, right = 1, n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(floor_sqrt(n))