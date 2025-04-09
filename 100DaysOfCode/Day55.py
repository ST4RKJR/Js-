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



#Delete the Kth node from the end
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteElement(head, k):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy

    # Move first pointer k+1 steps ahead
    for _ in range(k + 1):
        if first:
            first = first.next

    # Move both first and second until first reaches end
    while first:
        first = first.next
        second = second.next

    # Skip the target node
    second.next = second.next.next

    return dummy.next
