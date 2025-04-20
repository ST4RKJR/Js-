#Thala for a reason
n = int(input())
arr = list(map(int, input().split()))

count = sum(1 for x in arr if x % 7 == 0)

print(count)



#
