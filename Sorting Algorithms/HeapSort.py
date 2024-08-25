def heapify(a,n,i):
    lar = i
    l = 2*i + 1
    r = 2*i + 2
    
    if l<n and a[i] < a[l]:
        lar = l 
    if r<n and a[lar]<a[r]:
        lar = r 
    if lar!=i:
        (a[i],a[lar]) = (a[lar],a[i])
        heapify(a,n,lar)
        

def h(a):
    n = len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    
    for i in range(n-1,0,-1):
        (a[i],a[0]) = (a[0],a[i])
        heapify(a,i,0)


a = [1,12,9,5,6,10]
h(a)
for i in range(len(a)):
    print(a[i],end=" ")    
