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

def insert(n,d):
    if n is None:
        return Node(d)
    else:
        if d < n.v:
            n.l = insert(n.l,d)
        else:
            n.r = insert(n.r,d)
    return n
def minval(n):
    c=n
    while c.l is not None:
        c= c.l
    return c
    
def dele(n,d):
    if n is None:
        return n
    if d<n.v:
        n.l=dele(n.l,d)
    elif d>n.v:
        n.r = dele(n.r,d)
    else:
        if n.l is None:
            temp = n.r
            n = None
            return temp
        if n.r is None:
            temp = n.l
            n = None
            return temp    
        temp = minval(n.r)
        n.v = temp.v
        n.r = dele(n.r, temp.v)

    return n     

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
IN(root)

print("\nDelete 10")
root = dele(root, 10)
print("Inorder traversal: ", end=' ')
IN(root)
            
        
