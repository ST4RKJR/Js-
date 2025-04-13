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


