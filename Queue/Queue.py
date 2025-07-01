class Queue: 
    def __init__ (self):
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def isEmpty(self):
     if self.items ==[]:
            return True
        
     else:
        return False
    
    def enqueue(self, item):
         return self.list.append(item)
     
    def dequeue(self):
        if self.isEmpty():
            return None 
        else:
            return self.items.pop(0)
        
        
    
    
    
    
   
myQueue = Queue()

myQueue.items.append(1)
myQueue.items.append(2)
myQueue.items.append(3)

print(myQueue)  # Output: [1, 2]



print(myQueue.dequeue())
print(myQueue.dequeue())## Output: False