class StackArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)
    
    def isempty(self):
        return len(self.data) == 0
    
    def push(self, a):
        self.data.append(a)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None  
        return self.data.pop()

    def top(self):
        if self.isempty():
            print("Stack is empty")
            return None  
        return self.data[-1]

    def print_stack(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contents:", self.data)


s = StackArray()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()  
print(s.pop())   
s.print_stack()  
print(s.top())   
print(len(s))    
