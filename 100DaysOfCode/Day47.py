#Climbing Stairs (DP)
def climb(x):
    a , b = 1 ,1 
    for i in range(x):
        a ,b = b , (a+b) % ((10**9)+7) 
    return a

x = int(input())
print(climb(x))


