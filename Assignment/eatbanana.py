def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    
    while low < high:
        mid = (low + high) // 2
        time = 0
        for i in piles:
            time += (i + mid - 1) // mid

        if time <= h:
            high = mid 
        else:
            low = mid + 1
    return low