class Node:
    def __init__(self ,data):
        self.next = None
        self.data  = data
def reverse(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        # curr.next = curr
        curr.next = prev
        prev = curr
        # curr.next is now 1 
        
        curr = next
        # here curr is now on curr.next and we change
        # curr = next so thats why it run into infinite loop
        # curr = curr.next 

    return prev
def travserse(head):
    cuurr = head
    while cuurr != None:
        print(cuurr.data )
        cuurr = cuurr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head.next.next.next = Node(4)

head  = reverse(head)
travserse(head)

