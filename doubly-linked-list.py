class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

def List_traversal(head):
    currentNode=head
    while currentNode:
        print(currentNode.data,end="<->")
        currentNode=currentNode.next
    print(None)

def reverse_list_traversal(tail):
    currentNode=tail
    while currentNode:
        print(currentNode.data,end="<->")
        currentNode=currentNode.prev
    print(None)
    

head=Node(5)
n2=Node(4)
n3=Node(3)
n4=Node(2)

tail=n4


head.next=n2
n2.prev=head
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3


List_traversal(head)
reverse_list_traversal(tail)

