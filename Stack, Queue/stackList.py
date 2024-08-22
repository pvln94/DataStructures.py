class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class L:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size  
    
    def isempty(self):
        return self.size == 0

    def push(self,val):
        node=Node(val)
        node.next = self.top 
        self.top = node 
        self.size += 1

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return 

        popval = self.top.data 
        self.top = self.top.next 
        self.size -= 1 
        print(popval) 

    def peek(self):
        if self.isempty():
            print("Stack is empty")
            return      
        print(self.top.data) 

    def printstack(self):
        if self.isempty():
            print("Stack is empty")
            return 
        current = self.top 
        stack = []
        while current:
            stack.append(current.data)    
            current = current.next 
        print("Stack:",stack)     

s = L()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.peek()
s.printstack()

s.pop()
s.peek()
s.printstack()




