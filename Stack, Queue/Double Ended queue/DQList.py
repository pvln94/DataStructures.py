class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # To link to the previous node

class DequeLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def push_front(self, e):
        new_node = Node(e)
        if self.isempty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def push_back(self, e):
        new_node = Node(e)
        if self.isempty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self.size += 1

    def pop_front(self):
        if self.isempty():
            return None
        popped_value = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return popped_value

    def pop_back(self):
        if self.isempty():
            return None
        popped_value = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.size -= 1
        return popped_value

    def first(self):
        if self.isempty():
            return None
        return self.front.data

    def last(self):
        if self.isempty():
            return None
        return self.rear.data

    def print_queue(self):
        if self.isempty():
            print("Queue is empty")
            return
        current = self.front
        queue_elements = []
        while current:
            queue_elements.append(current.data)
            current = current.next
        print("Queue:", queue_elements)


q = DequeLinkedList()
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
