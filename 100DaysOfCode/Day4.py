#Minimum Size Subarray Sum K
def minSubArray(arr, k):
    l = len(arr)
    mini = float('inf')
    x = 0
    summ = 0

    for y in range(l):
        summ += arr[y]

        while summ >= k:
            mini = min(mini, y - x + 1)
            summ -= arr[x]
            x += 1

    if mini != float("inf"):
        return mini 
    else:
        return 0
    
#Prefix Removals
# Your code here
def longest_prefix_in_substring(s):
    n = len(s)
    for i in range(n):
        prefix = s[:i + 1]
        if s.find(prefix, i + 1) != -1:
            return i + 1 
    return 0 

def process_string(s):
    while True:
        x = longest_prefix_in_substring(s)
        if x == 0:
            break
        s = s[x:]
    return s

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0]) 
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        final_string = process_string(s)
        results.append(final_string)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()