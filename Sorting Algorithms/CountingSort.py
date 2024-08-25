def c(a):
    n = len(a)
    m = max(a)
    c = [0]* (m+1)
    o=[0]*n
    for i in range(0,n):
        c[a[i]] += 1
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    i=n-1
    while i>=0:
        o[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
        i-=1
    for i in range(n):
        a[i] = o[i] 
    print(a)    
    
a = [4, 2, 2, 8, 3, 3, 110]
c(a)