class Node:
    def __init__(self ,data):
        self.next = None
        self.data = data

def swap_data(head):
    curr = head
    while curr != None:
        curr.data , curr.next.data = curr.next.data , curr.data
        curr = curr.next.next
    return head

def traverse(head):
    curr = head
    while curr != None:
        print(curr.data ,end=" ")
        curr =curr.next

def swap_Ea(head):
    prev = head
    curr = head.next.next
    # prev.next = head
    head = head.next
    head.next = prev


head = Node(12)
head.next = Node(34)
head.next.next = Node(14)
head.next.next.next  = Node(13)
swap_data(head)
traverse(head)

