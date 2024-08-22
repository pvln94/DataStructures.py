
# init is a constructor/method which initializes objects of a class

#  self represent instance(occurance) of a class, it is used to access attributes and methods of a class

#SLL
class Node1:
    def __init__(self,data):
        self.data=data
        self.next = None

#DLL
class Node2:
    def __init__(self,data):
        self.data=data
        self.prev = None
        self.next = None

         