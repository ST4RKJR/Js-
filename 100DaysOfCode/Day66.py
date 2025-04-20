#Thala for a reason
n = int(input())
arr = list(map(int, input().split()))

count = sum(1 for x in arr if x % 7 == 0)

print(count)



#Count Subarrays with Max Value in Range
def numSubarrayBoundedMax(nums, left, right):
    def count(limit):
        c = 0 
        curr = 0 
        for i in nums:
            if i  <= limit:
                curr += 1
                c += curr
            else:
                curr = 0

        return c 

    maxRight = count(right)
    maxLeft = count(left - 1)
    return maxRight - maxLeft


class Solution:
    def numSubarrayBoundedMax(self, nums, left: int, right: int) -> int:
        
        def count_subarrays_with_max_atmost_x(x):
        
            front = count = 0

            for rear in range(len(nums)):

                if nums[rear] > x:

                    front = rear + 1
                    continue

                count += rear - front +1
            
            return count
         
        return count_subarrays_with_max_atmost_x(right) - count_subarrays_with_max_atmost_x(left-1)
		