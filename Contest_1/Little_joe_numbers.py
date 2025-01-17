nums = int(input())
arr = list(map(int,input().split()))

querries = int(input())

for i in range(querries):
    start , end = map(int,input().split())
    count = 0
    for j in range(start,end+1):
        if arr[j] % 3 == 0:
            count += 1
    print(count)