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
            return True  # Cycle detected

    return False  # No cycle