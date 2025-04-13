class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPositive(head):
    # Count the number of negative elements in the list
    negative_count = 0
    
    # Traverse the linked list
    current = head
    while current:
        if current.data < 0:
            negative_count += 1
        current = current.next
    
    # If the count of negative numbers is even, the product is positive
    if negative_count % 2 == 0:
        return "Yes"
    else:
        return "No"


n = int(input())
tokens = list(map(int, input().split()))
power = int(input())

tokens.sort()
left = 0
right = n - 1
max_score = 0
current_score = 0

while left <= right:
    if power >= tokens[left]:
        power -= tokens[left]
        current_score += 1
        left += 1
        max_score = max(max_score, current_score)
    elif current_score > 0:
        power += tokens[right]
        current_score -= 1
        right -= 1
    else:
        break

print(max_score)