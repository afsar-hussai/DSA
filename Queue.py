# queue is like we are standing in a ticket line, first  person will be out first and who comes new will be added to last of the line
## it is FIFO

## Linkedlist is the best way to implement it because to remove first element we don't need to move all left side elements
## here for just demonstration we are using a collection called deque. but actually we need to use linkedlist

from collections import deque

que=deque()
que.append(5)
que.append(4)
que.append(3)
que.append(2)

print(f"queue is : {que}")

x=que.popleft()

print(f"First element is {x} and new queue is: {que}")
