class Node:
    def __init__(self , data):
        self.next = None
        self.data = data
def reverse(head):
    curr = head 
    prev = None
    while curr != None:
        next = curr.next 
        curr.next = prev
        prev = curr
        curr = next

    return prev
def palindrome(head):
    curr = head
    slow = head
    fast = head
    while curr.next != None and curr.next.next != None:
        slow = slow.next 
        fast = fast.next.next
        curr = fast

    rev = reverse(slow.next)
    curr = head
    while rev != None:
        if curr.data != rev.data:
            return False
        curr = curr.next 
        rev = rev.next

        
    return True
head = Node("R")
head.next = Node("A")
head.next.next = Node("D")

head.next.next.next = Node("A")
head.next.next.next.next = Node("R")
head.next.next.next.next.next = Node("X")
print(palindrome(head))