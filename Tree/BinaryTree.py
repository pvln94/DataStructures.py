class Node:
    def __init__(self,v):
        self.l = None
        self.v = v
        self.r = None 

def IN(n):
    if n:
        IN(n.l)
        print(n.v,end=" ")
        IN(n.r)
def PRE(n):
    if n:
        print(n.v,end=" ")
        PRE(n.l)
        PRE(n.r)
def POST(n):
    if n:
        POST(n.l)
        POST(n.r)
        print(n.v,end=" ")
def c(n):
    if n is None:
        return 0
    return 1+c(n.l)+c(n.r) 
def H(n):
    if n is None:
        return 0
    left=H(n.l)
    right=H(n.r)
    return max(left,right)+1 

def isFull(n):
    if n is None:
        return 1
    if n.l is None and n.r is None:
        return 1
    if n.l is not None and n.r is not None:
        return (isFull(n.l)) and (isFull(n.r))
    return 0    

def isPerfect(n,d,level=0):
    if n is None:
        return 1
    if n.l is None and n.r is None:
        return d == level+1 
    if n.l is None or n.r is None:
        return 0 
    return isPerfect(n.l,d,level+1) and  isPerfect(n.r,d,level+1)

def isComplete(n,index,c):
    if n is None:
        return 1
    if index>=c:
        return 0
    return isComplete(n.l,2*index+1,c) and isComplete(n.r,2*index+2,c)   
def BalancedBinaryTree(n):
    if n is None:
        return 1
    
    left_height = H(n.l)
    right_height = H(n.r)
    
    if abs(left_height - right_height) > 1:
        return 0
    
    return BalancedBinaryTree(n.l) and BalancedBinaryTree(n.r)
        

r = Node(1)
r.l=Node(2)
r.r=Node(3)
r.l.l=Node(4)
r.l.r=Node(5)
r.r.l=Node(6)
r.r.r=Node(7)

print(IN(r))
print(PRE(r))
print(POST(r))
print(c(r))
print(H(r))
print(isFull(r))
print(isPerfect(r,H(r)))
index=0
print(isComplete(r,index,c(r)))
print(BalancedBinaryTree(r))
