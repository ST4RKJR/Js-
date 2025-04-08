#Detect Linked List Cycle
'''class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
'''
def detectCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True  

    return False 


#Intersection of two linked list
'''class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None'''

def intersection(head1, head2):
    if not head1 or not head2:
        return None

    ptr1 = head1
    ptr2 = head2

    while ptr1 != ptr2:
        ptr1 = ptr1.next if ptr1 else head2
        ptr2 = ptr2.next if ptr2 else head1

    return ptr1


class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # Cycle detected

        return False  # No cycle
        