class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    

def traverse_node(head):
        currentNode=head
        # print("Before while loop: ",currentNode,currentNode.data)
        
        while currentNode:
            # print("inside while loop: ",currentNode,currentNode.data)
            print(currentNode.data,end="-->")
            currentNode=currentNode.next
        # print("After while loop",currentNode)
        print("null")

def findMinValue(head):
    min_value=head.data
    CurrentNode=head.next
    #  print( min_value, CurrentNode.data)
    while CurrentNode:
        #   print("Values of min and current: ")
        #   print( min_value, CurrentNode.data)
          
        if CurrentNode.data < min_value:
            min_value=CurrentNode.data
        CurrentNode=CurrentNode.next
    return min_value

def insert_node(position,head,new_node):
    if position == 1:
        new_node.next=head
        return new_node
    currentNode=head
    # To get previous node of where we want to enter node
    for _ in range(position-2):
        if currentNode is not None:
            currentNode=currentNode.next
    # To check position is in range
    if currentNode is None:
        print("Position Out of bound")
        return head
    
    new_node.next=currentNode.next
    currentNode.next=new_node
    return head

def delete_node(head,nodeToDelete):
    
    if nodeToDelete == head:
        return head.next
    currentNode=head
    while currentNode.next and currentNode.next !=nodeToDelete:
        currentNode=currentNode.next
    
    if currentNode.next == None:
        print("Node doesn't exist")
        return head
    
    currentNode.next=currentNode.next.next
    return head
        
          
        

node1=Node(5)
node2=Node(7)
node3=Node(2)
node4=Node(8)
# print(node3.next)
# print(node4)

node1.next=node2
node2.next=node3
node3.next=node4
# print(node3.next)
print("List before Insertion\n")
traverse_node(node1)
print("min value is",findMinValue(node1))
new_nodee=Node(53)
node1=insert_node(2,node1,new_nodee)
print("\nList After Insertion")
traverse_node(node1)
# here node3 will be deleted (node3 is refrence to the address where node3 data is stored)
node1=delete_node(node1,node3)
print("\nList After Deletion")
traverse_node(node1)