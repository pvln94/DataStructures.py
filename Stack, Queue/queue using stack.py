class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Main stack for pushing elements
        self.stack2 = []  # Auxiliary stack for popping elements

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def isempty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, e):
        self.stack1.append(e)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def first(self):
        if self.isempty():
            print("Queue is empty")
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def print_queue(self):
        if self.isempty():
            print("Queue is empty")
            return
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        print("Queue:", self.stack2[::-1] + self.stack1)

# Example usage
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_queue()  # Should print: Queue: [1, 2, 3, 4]

q.dequeue()
q.print_queue()  # Should print: Queue: [2, 3, 4]

print(q.first())  # Should print 2
