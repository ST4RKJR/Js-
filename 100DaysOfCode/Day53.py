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

#Merge two sorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def Merge(head1, head2):
    dummy = Node(0)  
    current = dummy  
    
    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    
    if head1:
        current.next = head1
    else:
        current.next = head2
    
    return dummy.next


    
    
class Solution:
    def mergeTwoLists(self, list1):
        cur = dummy = 2
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next