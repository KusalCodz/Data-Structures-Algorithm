class Stack:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
    def delete(self):
        self.items = []
        print("Stack deleted")
#  // object instantiation and method calls   
myStack = Stack()
# adding elements to the stack
    
myStack.push(1)
myStack.push(2)
print(myStack)

#get the top element
myStack.pop()
print(myStack)


# checking the top element
print(myStack.peek())


# deleting the  stack
myStack.delete()