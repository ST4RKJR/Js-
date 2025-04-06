Q = int(input())
for _ in range(Q):
    l1, r1, l2, r2, X = map(int, input().split())
    n = l2 - l1 + 1  # number of diagonal steps
    sum_val = 0
    i = l1
    j = r1

    for k in range(n):
        val = (i + k)**2 + (j + k)**2
        if val % X == 0:
            sum_val += val
    print(sum_val)
    
    
#palindrome check 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True
    
    # Find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half
    prev = None
    current = slow
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    # Compare the first half and the reversed second half
    first = head
    second = prev
    while second:
        if first.val != second.val:
            return False
        first = first.next
        second = second.next
    
    return True


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head or not head.next:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    
    while current:
        # If current node has duplicates
        if current.next and current.val == current.next.val:
            # Skip all nodes with the same value
            duplicate_value = current.val
            while current and current.val == duplicate_value:
                current = current.next
            prev.next = current
        else:
            prev = prev.next
            current = current.next
    
    return dummy.next

#revised code
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def deleteDuplicates(head):
    if not head or not head.next:
        return head
    
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head
    
    while current:
        # If current node has duplicates
        if current.next and current.data == current.next.data:
            # Skip all nodes with the same value
            duplicate_value = current.data
            while current and current.data == duplicate_value:
                current = current.next
            prev.next = current
        else:
            prev = prev.next
            current = current.next
    
    return dummy.next