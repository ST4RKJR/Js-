## LONGEST INCREASING SUBSEQUENCE
def lengthOfLIS(nums):
    # memo = {}

    # def f(i):
    #     if i in memo:
    #         return memo[i]

    #     if i == 0:
    #         return 1

    #     maxi = 1
    #     for j in range(i):
    #         if nums[j] < nums[i]:
    #             maxi = max(maxi, f(j) + 1)
    #     memo[i] = maxi 
    #     return memo[i]

    # ans = 1
    # for i in range(1, len(nums)):
    #     ans = max(ans, f(i))
    # return ans

    memo = {}
    def f(i):
        if i in memo:
            return memo[i]
        
        if i == 0:
            return 1
        
        maxi = 1
        for j in range(i):
            if nums[j] < nums[i]:
                maxi = max(maxi, f(j) + 1)
        memo[i] = maxi
        return memo[i]

    ans = 1
    for i in range(1, len(nums)):
        ans = max(ans, f(i))
    return ans

## AVERAGE MARKS
n = int(input())
arr = [int(i) for i in input().split()]

print(sum(arr) // n)