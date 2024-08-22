class DE:
    def __init__(self):
        self.data =[]

    def __len__(self):
        return len(self.data)

    def isempty(self):
        return len(self.data) == 0   

    def push_front(self,e):
        self.data.insert(0,e)

    def push_back(self,e):
        self.data.append(e)

    def pop_front(self):
        if self.isempty():
            return None 
        return self.data.pop(0)
    
    def pop_back(self):
        if self.isempty():
            return None 
        return self.data.pop() 
    
    def first(self):
        if self.isempty():
            return None 
        return self.data[0] 
    
    def last(self):
        if self.isempty():
            return None 
        return self.data[-1] 
    
    def print_queue(self):
        if self.isempty():
            return None 
        else:
            print("Queue:", self.data ) 

q = DE()
q.push_back(1)
q.push_back(2)
q.push_back(3)
q.push_back(4)
q.push_back(5)
q.print_queue()

q.push_front(6)
q.print_queue()

q.pop_back()
q.print_queue()

q.pop_front()
q.print_queue()

print(q.first())
print(q.last())