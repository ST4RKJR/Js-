s = input()
c = input()
ans = -1
# rev = []
# for j in s:
#     rev.append(j)
# rev.sort()


for i in range(len(s)-1,-1,-1):
    if s[i] == c:
        ans = i
        break
print(ans)

maxi = 0
for i in range(len(s)):
    if s[i] == c:
        maxi = i 
        
if maxi == 0:
    print(-1)
else:
    print(maxi)