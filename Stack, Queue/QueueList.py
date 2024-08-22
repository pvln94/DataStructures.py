class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 

class L:
    def __init__(self):
        self.front = None 
        self.rear = None 
        self.size = 0 

    def __len__(self):
        return self.size 

    def isempty(self):
        return self.size == 0 

    def enqueue(self,v):
        node = Node(v)    
        if self.isempty():
            self.front = self.rear = node 
        else: 
            self.rear.next = node 
            self.rear = node  
        self.size += 1 

    def dequeue(self):
        if self.isempty():
            return None 
        
        dequeued_value = self.front.data 
        self.front = self.front.next
        if self.front is None:
            self.rear = None 
        self.size -= 1
        return dequeued_value
    
    def first(self):
        if self.isempty():
            return None 
        return self.front.data 
    
    def printqueue(self):
        if self.isempty():
            return None
        current = self.front 
        queue = []
        while(current):
            queue.append(current.data)
            current = current.next 
        print('Queue elements:',queue)    


q = L()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.printqueue() 

q.dequeue()
q.printqueue()

print(q.first())

                