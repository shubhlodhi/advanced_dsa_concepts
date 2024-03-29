class Node:
    def __init__(self, data):
        self.next  = None
        self.data = data
def revserse(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def traverse(head):
    curr = head
    while curr != None:
        print(curr.data , end="")
        curr = curr.next

def adding_ll_nodes(head ,head1):
    prev = revserse(head)
    prev1 = revserse(head1)
    # curr = head
    # curr1 = head1
    original = {None:None}
    # origi  
    prev3 = None
    sum =0
    curr = prev
    curr1 = prev1
    while prev != None and prev1 != None:
        if (prev1.data + prev.data) > 10:
         if sum >= 10:
            sum = prev.data+prev1.data-10
            # original.data = sum
            # original = original.next
            prev = prev.next
            prev1 = prev1.next

    return original






    # while curr != None and curr1 != None:


head = Node("1")
head.next = Node("2")
head.next.next = Node("3")

head1 = Node("1")
head1.next = Node("2")
head1.next.next = Node("3")
head = revserse(head)
traverse(head)
adding_ll_nodes(head , head1)