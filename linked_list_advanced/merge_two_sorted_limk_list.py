class Node:
   def __init__(self ,data):
      self.next = None
      self.data = data
def merge_LL(head1 , head2):
    curr1 = head1
    curr2 = head2
    tail = None
    if curr1.data < curr2.data:
        head = curr1
        tail = head
        curr1 = curr1.next

    else:
        head = curr2
        tail = head
        curr2 = curr2.next

    curr = head
    while curr1 != None and curr2 !=None:
     if curr1.data < curr2.data:
        tail.next = curr1
        
        curr1  = curr1.next
        tail = tail.next


     else:
        tail.next  = curr2
        curr2 = curr2.next
        tail = tail.next

    # tail.next = None
    if curr1 == None:
       tail.next = curr2

    else:
       tail.next = curr1

    # tail = head

    curr  = head 
    # for i in range(0,6):
    while curr != None:

        # curr = head
        print(curr.data)
        curr = curr.next
    return head

    

def traverse(head):
   curr = head
   while curr != None:
      print(curr.data)
      curr = curr.next
head = Node(35)
head.next = Node(38)
head.next.next = Node(39)

head1 = Node(24)
head1.next = Node(54)
head1.next.next = Node(84)

merge_LL(head , head1)
# traverse(head)


    