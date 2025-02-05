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
