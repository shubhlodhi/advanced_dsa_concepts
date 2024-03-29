from collections import deque
q = deque()
f,r =0,0
q.append('a')

q.append('b')
f+=1
q.append('c')
f+=1
print("Initial queue")
print(q)
print("\nElements dequeued from the queue")
print(q.popleft())
print(q)
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)