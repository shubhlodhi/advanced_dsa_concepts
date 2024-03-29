class node:
    def __init__(self ,data):
        self.next = None
        self.data = data

def insert_in_ll(head,data):
    temp = node(data)
    curr  = head
    while curr.next != None:
        if curr.next.data > temp.data:
         var = curr.next
         curr.next = temp
         temp.next = var
         break
        curr = curr.next

        # break
    # curr = curr.next


    return head
def prints(head):
    curr  = head
    while curr != None:
        print(curr.data,end="")

        curr = curr.next    
head = node(1)
head.next = node(2)
head.next.next = node(4)
insert_in_ll(head,3)
prints(head)
