from collections import deque

def count_students_unable_to_eat(n, students, sandwiches):
    student_queue = deque(students)
    sandwich_stack = sandwiches
    attempts = 0  # Count how many students in a row have passed

    while student_queue and attempts < len(student_queue):
        if student_queue[0] == sandwich_stack[0]:
            student_queue.popleft()
            sandwich_stack.pop(0)
            attempts = 0  # reset attempts when a student eats
        else:
            student_queue.append(student_queue.popleft())
            attempts += 1  # increment attempts when student doesn't eat

    return len(student_queue)

# Example usage
n = int(input())
students = list(map(int, input().split()))
sandwiches = list(map(int, input().split()))
print(count_students_unable_to_eat(n, students, sandwiches))



def max_subarray_sum(arr):
    max_current = max_global = arr[0]

    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(max_subarray_sum(arr))


class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = float('-inf')
        currentSum = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum > maxSum:
                maxSum = currentSum
            
            if currentSum < 0:
                currentSum = 0
        
        return maxSum