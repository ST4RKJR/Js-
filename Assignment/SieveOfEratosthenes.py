n = int(input())
sieve = [True] * (n+1)
sieve[0] = False
sieve[1] = True

for i in range(2,int(n**(0.5))+1):
    if sieve[i]:
        for multiple in range(2*i,n,i):
            sieve[multiple] = False
            
prime = []
for i in range(len(sieve)):
    if sieve[i]:
        prime.append(i)
print(*prime)