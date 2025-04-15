'''
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''
def deleteDuplicates(head):

    if head.next == None:
        return head
    temp = head
    while temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next 
        else:
            temp.next.prev = temp
            temp = temp.next

        

    return head


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insertion(head, K):
    temp = head
    while temp.next != head :
        temp = temp.next
    new_node = Node(K)
    temp.next = new_node
    new_node.next = head
    return head


def maxDepth(s):
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1
    
    return max_depth
