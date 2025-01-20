# n,q = map(int,input().split())
# string = input()
# pre = [0]*n
# count = 0
# for i in range(1,n):
#     if string[i]=="C" and string[i-1]=="A":
#         count+=1
#         pre[i]=pre[i-1]+1
#     else:
#         pre[i]=pre[i-1]

# for i in range(q):
#     x, y = map(int,input().split())
#     x = x-1
#     y = y-1
#     if x == 0:
#         print(pre[y])
#     else:
#         print(pre[y]-pre[x-1])


n,q = map(int,input().split())
string = input()
pre = []
count = 0
for i in range(len(string)):
    if string[i]=="C" and string[i-1]=="A":
        count+=1
        pre.append(count)
    else:
        pre.append(count)

for i in range(q):
    x, y = map(int,input().split())
    print(pre[y-1]-pre[x-1])