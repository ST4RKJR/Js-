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

'''
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
'''


def search_in_bst(root, key):
    if not root:
        return 0
    if root.data == key:
        return 1
    elif key < root.data:
        return search_in_bst(root.left, key)
    else:
        return search_in_bst(root.right, key)