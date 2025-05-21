## Cost of Stock 

n = int(input())
a = list(map(int, input().split()))
ans = []
l = 0

for r in range(1, n):
    if a[r] < a[r - 1]:
        if l < r - 1:
            ans.append((l, r - 1))
        l = r

if l < n - 1:
    ans.append((l, n - 1))

if not ans:
    print("null")
    exit()

for l, r in ans:
    print(l, r)
    
    
## ADD TWO NUMBERS


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addNumber(l1, l2): 
    dummy = Node(0)
    temp = dummy

    tot = 0
    carry = 0
    while l1 or l2 or carry:
        tot = carry 

        if l1:
            tot += l1.data 
            l1 = l1.next

        if l2:
            tot += l2.data 
            l2 = l2.next
        
        temp.next = Node(tot % 10)
        temp = temp.next 
        carry = tot // 10 
    
    return dummy.next