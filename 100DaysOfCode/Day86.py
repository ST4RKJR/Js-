#Find Node Position
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

def node_position(head, X):
    position = 1
    curr = head
    while curr is not None:
        if curr.value == X:
            return position
        curr = curr.next
        position += 1
    return position
