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