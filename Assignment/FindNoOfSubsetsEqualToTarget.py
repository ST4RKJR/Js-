# array = [10,20,20,5,15]
# target = 30
# count = 0
# for i in range(len(array)):
#     for j in range(i+1,len(array)):
#         if i == len(array)-1:
#             if array[i] == target:
#                 count += 1
#         elif array[i] + array[j] == target:
#             count += 1
# print(count)
             
def countSubsets(lis,curr_index,target):
    #base case
    if target == 0 :
        return 1
    if curr_index == len(lis):
        return 0
    #recursive case
    #if curr elements is picked
    ans1 = countSubsets(lis,curr_index+1,target - lis[curr_index])
    #if curr element is not picked
    ans2 = countSubsets(lis,curr_index+1,target)
    return ans1+ans2
        
        
n,k = map(int,input().split())
lis = list(map(int,input().split()))
ans = countSubsets(lis,0,k)
print(ans)