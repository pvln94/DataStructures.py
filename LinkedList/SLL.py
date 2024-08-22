#  At begining
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ll:
    def __init__(self):
        self.head = None


    def insertAtBeg(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
            
# at any pos
    def insertAtIndex(self,data,index):
        if(index==0):
            return self.insertAtBeg(data)

        pos = 0
        current=self.head
        while(current != None and pos+1 != index):
            pos += 1
            current = current.next

        if current!= None:
            node = Node(data)
            node.next = current.next
            current.next = node            
        else:
            print("Invalid index")         

# at end
    def insertAtEnd(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head =  new_node
            return

        current = self.head
        while(current.next):
            current = current.next    
        current.next = new_node  

# Updation of one value to another value
    def update(self,value,index):
        pos = 0
        current = self.head

        if index == pos:
            current.data = value 

        while(current!=None and pos != index):
            pos += 1
            current = current.next

        if current != None:
            current.data = value
        else:
            print("Invalid index")                      
        


# Deletion

# At beg
    def delAtBeg(self):
        if self.head is None:
            return
        self.head = self.head.next

#At end
    def delAtEnd(self):
        if self.head is None:
            return
        
        current = self.head

        while(current.next != None and current.next.next!=None):
            current = current.next

        current.next = None

#At any index
    def delAtIndex(self,index):
        if self.head is None:
            return
        
        pos = 0
        current = self.head
        if pos==index:
            return self.delAtBeg()


        while(current!=None and pos +1 != index):
            pos += 1
            current = current.next

        if current != None:
            current.next = current.next.next
        else:
            print('Index not present')        

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

# print LL
    def printLL(self):
        current = self.head
        while(current):
            print(current.data,end="->")
            current = current.next
        print("None")    

#size of LL
    def size(self):
        size = 0
        if(self.head):
            current = self.head
            while(current):
                size += 1
                current = current.next
            print("Size is",size)
        else:
            return 0

a = ll()
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