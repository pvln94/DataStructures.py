def c(a,p):
    n=len(a)
    m=max(a)
    o=[0]*n
    c=[0]*(m+1)
    for i in range(n):
        b = a[i]//p
        c[b%10]+=1
    for i in range(1,len(c)):
        c[i] += c[i-1]
    
    i=n-1
    while i>=0:
        b=a[i]//p
        o[c[b%10]-1] = a[i]
        c[b%10] -= 1
        i-=1
    for i in range(n):
        a[i] = o[i]
        

def r(a):
    m = max(a)
    p=1
    while m//p > 0:
        c(a,p)
        p *= 10
    print(a)    

a = [121, 432, 564, 23, 1, 45, 788]
r(a)