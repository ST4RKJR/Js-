#Merge Linked List
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    current = l1
    while current.next:
        current = current.next
    current.next = l2
    return l1