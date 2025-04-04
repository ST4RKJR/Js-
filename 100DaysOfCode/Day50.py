#Merge By Parity
n , m = map(int,input().split())
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

i,j = 0,0
merged = []

while i < len(arr) or j < len(brr):
    if j == len(brr) or (i < len(arr) and arr[i] <= brr[j]):
        merged.append(arr[i])
        i += 1
    else:
        merged.append(brr[j])
        j += 1


even = []
odd = []

for i in merged:
    if i % 2 == 0 :
        even.append(i)
    else:
        odd.append(i)

answer = even + odd
print(*answer)