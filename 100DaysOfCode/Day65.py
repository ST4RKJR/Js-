'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

def count_nodes(head):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count +=1 
    return count


def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return "NO"
        else:
            stack.append(char)
    return "YES" if not stack else "NO"
n = int(input())
results = []
for _ in range(n):
    s = input()
    results.append(is_balanced(s))
for result in results:
    print(result)
