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

