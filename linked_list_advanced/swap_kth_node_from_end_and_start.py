class Node:
    def __init__(self ,data):
        self.next = None
        self.data = data

def reverse(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next 
        curr.next = prev
        prev = curr
        curr = next
        # curr = curr.next
def swap_Kth_nodes(head ,k):
    curr = head
    k1 =1
    left_kth_node =None
    while curr != None:
        if k1 == k:
           left_kth_node = Node(curr.data)
           left_kth_node = curr
        #    break

        curr =curr.next
        k1+=1


    s = reverse(head)
    rev_head  = s
    k1 = 1
    right_most_node =None
    while rev_head != None:
        if k1 == k:
            right_most_node = Node(rev_head.data) 
            right_most_node =  rev_head
            # break

        rev_head =rev_head.next 
        k1+=1

    # curr.data,rev_head.data = rev_head.data ,curr.data
    right_most_node , left_kth_node  = left_kth_node , right_most_node
    # curr2 = head
    # while curr2 != None:
         
    # for i in range(5):
def trav(head):
    curr = head
    while curr != None:
        print(curr.data ,end=" ")
        curr = curr.next
def count_nodes(head):
    count =0
    curr =head
    while curr.next != None:
        count+=1
        curr = curr.next

    return count
def swap_nodes(head,k):
    n = count_nodes(head)
    res =None
    prev = None
    temp = None
    if k>n:
        return
    
    prev_nodes = Node(None)
    # curr = head
    x =head
    

    for i in range(0,k-1):
        prev_nodes = x
        # curr =curr.next  
        x = x.next
    # curr =head
    prev_nodes_2 = Node(None)
    y = head
    for i in range(0,n-k):
        prev_nodes_2 =  y
        y = y.next
    
    # if res == None:
        # res = y

    if prev_nodes is not None:
        prev_nodes.next = y

    if prev_nodes_2 is not None:
        prev_nodes_2.next = x

    temp = x.next
    x.next = y.next
    y.next = temp






    

    






head = Node(12)
head.next = Node(13)
head.next.next  = Node(23)
# head.next.next.next.next = Node(14)

swap_Kth_nodes(head,2)
trav(head)
        