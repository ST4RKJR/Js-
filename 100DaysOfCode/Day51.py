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