class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LL:
    def __init__(self):
        self.head = None

# at Beggining
    def insertAtBeg(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

# at any pos
    def insertAtIndex(self,data,index):
        if(index == 0):
            return self.insertAtBeg(data)
        
        pos = 0
        current = self.head
        while(current!=None and pos+1 != index):
            pos += 1
            current = current.next

        if(current!=None) :
            node = Node(data)
            node.next = current.next
            node.prev = current

            if current.next!=None:
                current.next.prev = node
            current.next = node       

# at end
    def insertAtEnd(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
            node.prev = current
  

# Updation of one value to another value
    def update(self,val,index):
        pos = 0
        current = self.head
        if index == pos:
            current.data = val

        while(current != None and pos != index):
            pos+=1
            current = current.next

        if(current!=None):
            current.data = val
        else:
            print("Index not found")    

# Deletion
# At beg
    def delAtBeg(self):
        if self.head is None:
            return 
        self.head = self.head.next 

        if self.head is not None:
            self.head.prev = None     

# At End
    def delAtEnd(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
        
        current = self.head
        while(current.next.next!=None):
            current = current.next

        current.next = None           

# At any Index
    def delAtIndex(self,index):
        if(self.head is None):
            return 
        if(self.head.next is None):
            self.head = None
            return 
        pos = 0
        current = self.head

        if pos == index:
            return self.delAtBeg()

        while(current!=None and pos+1!=index):
            pos+=1
            current = current.next
        if(current!=None and current.next!=None):
            if current.next.next!=None:
                current.next.next.prev = current

            current.next = current.next.next
             
        else:
            print('Index not found')    

# remove particular node
    def remove_node(self,data):
        current = self.head 
        if current.data == data:
            self.delAtBeg()
            return 
        while(current!=None and current.next.data != data):
            current = current.next 
        if current is None:
            return None 
        else:
            current.next = current.next.next
            current.next.prev = current  

# print LL
    def printLL(self):
        current = self.head  
        if current is None:
            return 
        
        while(current):
            print(current.data,end="<->" if current.next!=None else "<->")
            current = current.next 
        print("None")

#size of LL 
    def size(self):
        size = 0
        if(self.head):
            current=self.head
            while(current):
                size+=1
                current = current.next 
            print("Size is",size)    
        else:
            return 0 
a = LL()        
a.insertAtEnd(1) 
a.insertAtEnd(2) 
a.insertAtEnd(3) 
a.insertAtBeg(4)
a.printLL()
a.insertAtIndex(5,1)
a.printLL()
a.size()

a. delAtBeg()
a.delAtEnd()
a.delAtIndex(1)
a.printLL()
a.size()
a.update(3,1)
a.printLL()
a.remove_node(5)
a.printLL()
a.size()