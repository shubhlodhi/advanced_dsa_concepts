class Node:
    def __init__(self , data):
        self.next = None
        self.data  = data
def print(head):
    curr = head
    while curr != None:
        print(curr.data , end=" ")
def merge_K_LL(a,k):
    for i in range(1 , k+1):
        head_0 = a[0]
        head_i = a[i]
        while(True):
            if head_0.data >= head_i.data:
                a[i] = head_i.next
                head_i.next  = head_0
                a[0] = head_i
                




    return