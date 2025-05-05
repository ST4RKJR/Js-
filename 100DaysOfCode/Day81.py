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
