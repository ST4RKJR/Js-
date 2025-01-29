a, b = map(int,input().split())
MOD = (10**9)+7
mul = 1
for i in range(b):
    mul *= a
print(mul % MOD)


#by recursion 
def exponentiation(a,b):
    if b == 0:
         return 1 
    return (exponentiation(a,b-1)*a) % ((10**9) + 7)

def power(a,b):
    if b == 0 :
        return 1
    x = exponentiation(a,b//2)
    if b % 2 == 1:
        return x * x * a
    else:
        return x * x    
    