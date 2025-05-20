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