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


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def max_num(head: Node) -> int:
    max_number = float('-inf')
    current = head
    current_number = ""

    while current:
        if current.val == -1:
            if current_number:
                max_number = max(max_number, int(current_number))
                current_number = ""
        elif 0 <= current.val <= 9:
            current_number += str(current.val)
        current = current.next

    # In case the list ends without another -1
    if current_number:
        max_number = max(max_number, int(current_number))

    return max_number


def depth_of_string_stack(s):
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            if current_depth > 0:
                current_depth -= 1
    return max_depth