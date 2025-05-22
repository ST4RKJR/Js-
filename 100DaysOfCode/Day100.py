## LONGEST SUBSTRING WITHOUT REPEATING
def longestUniqueSubstring(s):

    d = [0] * 26
    l = 0
    n = len(s)
    ans = 0

    for r in range(n):
        d[ord(s[r]) - 97] += 1
        while d[ord(s[r]) - 97] > 1:
            d[ord(s[l]) - 97] -= 1
            l += 1
        
        ans = max(ans, r - l + 1)

    return ans


## 100 DAYS OF CODE ENDS!!
def max_students(results, k):
    n = len(results[0])
    for i, arr in enumerate(results):
        zeros = n - sum(arr)
        results[i] = zeros
    
    results.sort()

    cnt = 0
    for i in results:
        if i == 0:
            cnt += 1
            continue 
        
        if i <= k:
            cnt += 1
            k -= i 
            continue

        break
    return cnt