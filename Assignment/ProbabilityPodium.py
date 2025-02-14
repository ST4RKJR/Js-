import math

def comb(n, k):
    # """Computes the combination n choose k (nCk)"""
    if k > n or k < 0:
        return 0
    return math.comb(n, k)

def solve():
    # Read input
    n, i, g, r = map(int, input().split())
    
    # Validate the input constraints
    if n < 3 or i < 1 or i > n or g < 0 or g > n or r < 0 or r > min(g, 3):
        print(-1)
        return
    
    # Total ways to select 3 coders from n
    total_ways = comb(n, 3)
    
    # 1. Probability that C_i makes it to the podium
    # If C_i is on the podium, we need to select 2 more coders from the remaining n-1
    ways_Ci_on_podium = comb(n-1, 2)
    prob_Ci_on_podium = ways_Ci_on_podium / total_ways
    
    # 2. Probability that exactly r coders from G make it to the podium
    # We need to select exactly r from G and 3-r from the other coders
    ways_exactly_r_from_G = comb(g, r) * comb(n - g, 3 - r)
    prob_exactly_r_from_G = ways_exactly_r_from_G / total_ways
    
    # Print the results rounded to 6 decimal places
    print(f"{prob_Ci_on_podium:.6f} {prob_exactly_r_from_G:.6f}")

# Call solve function to execute the logic
solve()