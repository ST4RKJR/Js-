dictionary = {}
dictionary[0] = 0
dictionary[1] = 1


def fib(x):
    if x in dictionary:
        return dictionary[x]
    ans = fib(x-1)+fib(x-2)
    dictionary[x]=ans
    return ans
    
def fib_old(n):
    if n <= 1:
        return n 
    return fib_old(n-1)+fib_old(n-2)

print(fib(199))