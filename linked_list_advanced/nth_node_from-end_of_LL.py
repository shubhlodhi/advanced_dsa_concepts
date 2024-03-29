class Node:
    def  __init__(self , data):
        self.next = None
        self.data = data

    

def reverse(head):
    curr = head
    temp = None
    while curr != None:
        # temp.next = curr
        next = curr.next
        # temp.next = curr
        next.next = curr

        curr.next = next
        # temp = curr.next
def nth_node_from_end(head ,n):
    curr = head
    # while curr != None:
    s = reverse(head)


        
