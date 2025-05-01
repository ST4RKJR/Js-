'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

def count_occurrences(head, K):
    count = 0
    current = head
    while current:
        if current.data == K:
            count += 1
        current = current.next
    return count