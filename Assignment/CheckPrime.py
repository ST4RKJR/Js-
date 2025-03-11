n = int(input())
def checkPrime(x):
    for i in range(2,int(x**(0.5))+1):
        if x % i == 0:
            return False
    return True

for i in range(2,n+1):
    if checkPrime(i):
        print(i,end=" ")