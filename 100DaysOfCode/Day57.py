def removeOuterParentheses(S):
    stack = []
    result = []
    start = 0 

    for i, ch in enumerate(S):
        if ch == '(':
            stack.append(ch)
        else:
            stack.pop()
            if not stack:
                result.append(S[start + 1:i])
                start = i + 1

    return "".join(result)

S = input()
print(removeOuterParentheses(S))


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        
        return "".join(res)
    
    
    
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def pairSum(head, K):
    # Initialize pointers to the beginning and end of the list
    left = head
    right = head

    # Move the right pointer to the last node
    while right.next:
        right = right.next

    count = 0

    # Traverse the list with two pointers
    while left != right and left.prev != right:
        current_sum = left.data + right.data
        if current_sum == K:
            count += 1
            left = left.next
            right = right.prev
        elif current_sum < K:
            left = left.next
        else:
            right = right.prev

    return count
