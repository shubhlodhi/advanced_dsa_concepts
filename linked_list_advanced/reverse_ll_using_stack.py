class Node:
    def __init__(self ,data ):
        self.data = data
        self.next = None

def insert_at_end(head ,node):
    nodes = Node(node)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = nodes

def traverse(head):
    curr = head 
    while curr != None:
        print(curr.data ,end=" ")
        curr = curr.next
        

def reverse_LL(head):
    stack = []
    curr = head
    while curr != None:
        stack.append(curr.data)
        curr = curr.next


    curr = head
    while curr != None:
        curr.data = stack.pop()
        curr  = curr.next


    return head
def reverse_LL_2(head):
    curr = head
    # if curr == None:
    #     print(curr.data)
    if curr != None:
        # print(curr.data)

        reverse_LL_2(head.next)
        print(curr.data ,end=" " )


    return head

def revrse_LL_at_k(head  ):
    curr = head
    # i =0
    # next = None
    prev = None

    while curr != None:
        next  = curr.next
        curr.next = prev
        prev = curr
        curr = next
        # curr = curr.next
    return prev
# def reverse_LL_at_k_position(head ,k):


    # while curr != None:
        # print(curr.data)
        # curr = curr.next

    # return prev
# def reverse_at_position(head,k):
    # curr = head
    # stack = []
    # i =0
    # while curr != None and i<k:
        # stack.append(curr.data)

        # curr = curr.next
    
    

    


    

        
        

head = Node(10)
head.next = Node(20)
insert_at_end(head ,30 )
insert_at_end(head , 90)
# traverse(head)
# reverse_LL(head)
# traverse(head)
# reverse_LL_2(head)
head = revrse_LL_at_k(head)
traverse(head)

