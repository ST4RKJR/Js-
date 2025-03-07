#Subset Target Sum (Recursion)
def subset_sum_exists(nums, target_sum):
    n = len(nums)
    
    def backtrack(i, curr_sum):
        if curr_sum == target_sum:
            return True
        if i >= n or curr_sum > target_sum:
            return False
        return backtrack(i + 1, curr_sum + nums[i]) or backtrack(i + 1, curr_sum)

    return backtrack(0, 0)

N = int(input())
nums = list(map(int, input().split()))
target_sum = int(input())

print("true" if subset_sum_exists(nums, target_sum) else "false")

