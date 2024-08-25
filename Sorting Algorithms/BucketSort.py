def b(a):
    b=[]
    for i in range(len(a)):
        b.append([]) #buckets 
    for i in a:
        j = int(10*i)
        b[j].append(i)
    for i in range(len(b)):
        b[i] = sorted(b[i])
    k=0
    for i in range(len(a)):
        for j in range(len(b[i])):
            a[k] = b[i][j]
            k+=1
    print(a)        

a = [.42, .32, .33, .52, .37, .47, .51]
b(a)