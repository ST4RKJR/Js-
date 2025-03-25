#Climbing Stairs (DP)
def climbTree(n):
    a,b = 1,1
    for i in range(n):
        mod = 10**9
        a,b = b , (a+b) % (mod+7)
    return a 

n = int(input())
print(climbTree(n))