#LIFO structure means which we Last in in stack that comes out First

# We can use dynamic array and linkedlist also, but linked list is best.
# for learning we are using just dynamic array

stack1=[]

stack1.append(5)
stack1.append(4)
stack1.append(3)
stack1.append(2)

print(f"Stack is : {stack1}")

x=stack1.pop()

print(f"last element is: {x} and new stack is : {stack1}")

## Peek is to find which element is top on stack

## isEmpty is to find something in stack is there or not to check before peek
if stack1:
    print(True)

    print(f"Peek of stack is: {stack1[-1]}")
else:
    print(False)

