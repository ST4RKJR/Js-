#Insert node at given position
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addElement(head, M, K):
    new_node = Node(K)
    
    # If insertion is at the beginning
    if M == 1:
        new_node.next = head
        return new_node
    
    current = head
    # Move to the (M-1)th node
    for _ in range(M - 2):
        if current is not None:
            current = current.next

    if current is None:
        return head  # This shouldn't happen due to constraints, but safety check

    # Insert new node after current
    new_node.next = current.next
    current.next = new_node
    
    return head
