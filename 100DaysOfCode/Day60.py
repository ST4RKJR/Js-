target = int(input())
nums = list(map(int, input().split()))

min_length = float('inf')
left = 0
current_sum = 0

for right in range(len(nums)):
    current_sum += nums[right]
    while current_sum >= target:
        min_length = min(min_length, right - left + 1)
        current_sum -= nums[left]
        left += 1

print(min_length if min_length != float('inf') else 0)


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def max_list(num1, num2):
    def linked_list_to_str(node):
        result = ''
        while node:
            result += str(node.value)
            node = node.next
        return result

    str1 = linked_list_to_str(num1)
    str2 = linked_list_to_str(num2)

    # Compare based on length first
    if len(str1) > len(str2):
        return int(str1)
    elif len(str2) > len(str1):
        return int(str2)
    else:
        # Same length, compare lexicographically
        return max(int(str1), int(str2))
    
    
    
class Solution:
    def minSubArrayLen(self, k: int, arr) -> int:
        l = len(arr)
        mini = float('inf')
        x = 0
        summ = 0

        for y in range(l):
            summ += arr[y]

            while summ >= k:
                mini = min(mini, y - x + 1)
                summ -= arr[x]
                x += 1

        if mini != float("inf"):
            return mini 
        else:
            return 0
        
