def fun(x):
    s = set(x)
    print(len(s))
    c = [0] * len(x)
    for i in range(len(x)):
        c[i] = 0
        for j in range(len(x)):
            if x[i] == x[j]:
                c[i] += 1
    print(c)            

if __name__ == "__main__":
    x = [112,1123,132,112]
    fun(x) 