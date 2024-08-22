class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insertAtBeg(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    # Insert at Any Index
    def insertAtIndex(self, data, index):
        if index == 0:
            return self.insertAtBeg(data)

        pos = 0
        current = self.head
        while current is not None and pos + 1 != index:
            pos += 1
            current = current.next
            if current == self.head:  # Completed a full circle
                print("Invalid index")
                return

        if current is not None:
            node = Node(data)
            node.next = current.next
            node.prev = current
            if current.next != self.head:
                current.next.prev = node
            current.next = node
        else:
            print("Invalid index")

    # Insert at End
    def insertAtEnd(self, data):
        if self.head is None:
            return self.insertAtBeg(data)

        new_node = Node(data)
        last = self.head.prev
        new_node.next = self.head
        new_node.prev = last
        last.next = new_node
        self.head.prev = new_node

    # Update Value
    def update(self, value, index):
        pos = 0
        current = self.head
        if index == pos:
            current.data = value
            return

        while current is not None:
            if pos == index:
                current.data = value
                return
            pos += 1
            current = current.next
            if current == self.head:  # Completed a full circle
                break
        print("Invalid index")

    # Delete at Beginning
    def delAtBeg(self):
        if self.head is None:
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
        else:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next

    # Delete at End
    def delAtEnd(self):
        if self.head is None:
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
            return

        last = self.head.prev
        last.prev.next = self.head
        self.head.prev = last.prev

    # Delete at Any Index
    def delAtIndex(self, index):
        if self.head is None:
            return

        pos = 0
        current = self.head
        if index == 0:
            return self.delAtBeg()

        while current is not None:
            if pos + 1 == index:
                current.next = current.next.next
                if current.next != self.head:
                    current.next.prev = current
                return
            pos += 1
            current = current.next
            if current == self.head:  # Completed a full circle
                break
        print('Index not present')

    # Remove Particular Node
    def remove_node(self, data):
        if self.head is None:
            return

        current = self.head
        if current.data == data:
            return self.delAtBeg()

        while current is not None:
            if current.data == data:
                current.prev.next = current.next
                if current.next != self.head:
                    current.next.prev = current.prev
                return
            current = current.next
            if current == self.head:  # Completed a full circle
                break
        print("Node with data not found")

    # Print CLL
    def printCLL(self):
        if self.head is None:
            print("None")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("Head")

    # Size of CLL
    def size(self):
        size = 0
        if self.head is None:
            print("Size is", size)
            return

        current = self.head
        while True:
            size += 1
            current = current.next
            if current == self.head:
                break
        print("Size is", size)
        return size

# Example Usage
a = CLL()
a.insertAtEnd(1) 
a.insertAtEnd(2) 
a.insertAtEnd(3) 
a.insertAtBeg(4)
a.printCLL()
a.insertAtIndex(5, 1)
a.printCLL()
a.size()

a.delAtBeg()
a.delAtEnd()
a.delAtIndex(1)
a.printCLL()
a.size()
a.update(3, 1)
a.printCLL()
a.remove_node(5)
a.printCLL()
a.size()
