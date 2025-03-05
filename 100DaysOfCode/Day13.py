#Print target sum subsets
#Check if N is Power of 4
n = int(input())

if n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0:
    print("True")
else:
    print("False")