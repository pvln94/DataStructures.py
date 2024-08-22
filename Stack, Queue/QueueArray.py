class QueueArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0

    def enqueue(self,val):
        self.data.append(val) 

    def dequeue(self):
        if self.isempty():
            return 
        return self.data.pop()

    def first(self):
        if self.isempty():
            return 
        return self.data[0]
    
    def print_queue(self):
        if self.isempty():
            return 
        else:
            print("Queue elements:", self.data)

q = QueueArray()
q.enqueue(1)     
q.enqueue(2)  
q.enqueue(3)  
q.enqueue(4)
q.print_queue()

q.dequeue()
q.print_queue()
print(q.first())