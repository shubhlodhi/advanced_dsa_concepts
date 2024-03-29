class Node:
    def __init__(self , data):
        self.next = None
        self.data = data


def even_odd_LL(head):
    curr = head
    while curr != None:
        # datas = curr.data
        if curr.data%2 ==0:
            first_head = head
            curr.data , first_head.data = first_head.data,curr.data
            first_head = first_head.next
            curr = curr.next

        curr = curr.next

        
    return head


def traverse(head):
    curr = head
    while curr != None:
        print(curr.data , end=" ")
        curr  = curr.next


def insert_at_middle(head , node):
    nodes = Node(node)
    curr = head
    while curr.next != None:
        curr  = curr.next
    curr.next = nodes

    return head


head = Node(12)
insert_at_middle(head , 13)
insert_at_middle(head , 90)
insert_at_middle(head , 33)
# traverse(head)
even_odd_LL(head)
traverse(head)



