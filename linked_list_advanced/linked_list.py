class LL:
    def __init__(self, data):
        self.head = None
        self.data = data

def reverse_at_k(head,k):
    curr = head

    i =0
    while curr != None and i != k :
        curr = curr.next
        i = i+1
        






s = LL("datp")
print(s.data)