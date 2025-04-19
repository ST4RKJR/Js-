'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''

def count_nodes(head):
    count = 0
    temp = head
    while temp:
        temp = temp.next
        count +=1 
    return count