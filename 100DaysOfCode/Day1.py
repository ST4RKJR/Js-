#Kth largest element in an Array


#It will work for large time limit
# def findKthLargest(nums, k):
#     copy = nums
#     new = []
#     for i in range(k-1):
#         new.append(max(copy))
#         copy.remove(max(copy))
#     return max(copy)

#It will work in shorter time period
def findKthLargest(nums, k):
    nums.sort()
    return nums[-k]



#100 Days of Code Begins
n = int(input())
if n == 1 :
    print("Congratulations! You've completed Day 1!")
else:
    print(f"You're on Day {n} of the challenge! Keep going!")