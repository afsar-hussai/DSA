class Node:
    def __init__(self,data,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev
    def __str__(self):
        return str(self.data)
    

reverse=[]
def reversee(head):
    currentNode=head
    if currentNode == None:
        return
    reversee(currentNode.next)
    reverse.append(currentNode)
    # print(currentNode)
    
def print_list(head):
    currentNode=head
    print(None)
    while currentNode:
        print(currentNode,end='<->')
        currentNode=currentNode.next
    print(None)
        
head=Node(5)
node2=Node(4)
node3=Node(3)
node4=Node(2)

head.next=node2
node2.next=node3
node3.next=node4

node2.prev=head
node3.prev=node2
node4.prev=node3
reversee(head)

print('<->'.join(str(x) for x in reverse))
print_list(head)


    
    
        