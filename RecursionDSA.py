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

#sum of numbers from 1  to n 
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
print(sum(5))


#find the highest marks of this give list of students of class
class_marks = [78,66,98,89,55,80]

def add(list):
    return list[0] + add(list[1::])
print(add(class_marks))