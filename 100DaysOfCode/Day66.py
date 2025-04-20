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