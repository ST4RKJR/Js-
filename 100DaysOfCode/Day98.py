## LUCKY NUMBER
n = int(input())
s = input()

first = 0
for i in range(n):
    first += int(s[i])

second = 0
for i in range(n, 2 * n):
    second += int(s[i])

print("LUCKY" if first == second else "UNLUCKY")

## ROmAN NUMBER TO INTEGER

def romanToInt(s):
    d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    
    ans = 0
    for i in range(len(s)):
        if i + 1 < len(s) and d[s[i]] < d[s[i + 1]]:
            ans -= d[s[i]]
        else:
            ans += d[s[i]]
        
    return ans