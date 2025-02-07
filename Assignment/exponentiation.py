mod  = (10*9)+7
def power_mod(a,b,mod):
    result = 1
    a = a%mod
    while b:
        if b%2:
            result = (result*a)%mod
        a = (a*a)%mod
        b//=2
    return result

















# mod = (10*9)+7
# def power_mod(a,b,mod):
#     result = 1
#     a %= mod
#     while b:
#         if b % 2:
#             result = (result*a)%mod
#         a = (a*a)%mod
#         b //= 2
#     return result
    
# a,b = 2,5
# print(power_mod(a,b,mod),"l")