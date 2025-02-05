#Infinite Loop 

# def a():
#     print("inside a ")
#     a()
# a()


# add = 0
# def sum_nums(x):
#     add += x
#     sum_nums(y)
# i = int(input())
# print(sum_nums(i))

arra = 1897132
def summ(arra):
    if arra == 0:
        return 0
    return arra%10+summ(arra//10)
print(summ(arra))


def fact(x):
    if x <= 1:
        return 1
    return x*fact(x-1)

print(fact(3))