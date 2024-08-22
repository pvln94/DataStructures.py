from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()  # Main queue for pushing and popping elements
        self.queue2 = deque()  # Auxiliary queue for internal reordering

    def __len__(self):
        return len(self.queue1)

    def isempty(self):
        return len(self.queue1) == 0

    def push(self, e):
        self.queue2.append(e)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        return self.queue1.popleft()

    def top(self):
        if self.isempty():
            print("Stack is empty")
            return None
        return self.queue1[0]

    def print_stack(self):
        if self.isempty():
            print("Stack is empty")
            return
        print("Stack:", list(self.queue1))

# Example usage
s = StackUsingQueues()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.print_stack()  # Should print: Stack: [4, 3, 2, 1]

s.pop()
s.print_stack()  # Should print: Stack: [3, 2, 1]

print(s.top())  # Should print 3
