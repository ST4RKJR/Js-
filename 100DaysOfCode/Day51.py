#Finding middle element
'''
class node :
    def __init__(data) :
    self.data = data
    self.next = None
'''
def findMid(head) :

    if not head:
        return -1

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data


#Insert node at at given position
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

def addElement(head, M, K):
    new_node = Node(K)
    
    if M == 1:
        new_node.next = head
        return new_node

    current = head
    for _ in range(M - 2):
        current = current.next

    new_node.next = current.next
    current.next = new_node
    
    return head