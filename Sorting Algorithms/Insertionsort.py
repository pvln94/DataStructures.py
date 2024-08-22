# Algorithm

def Insertionsort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

A= [1,4,2,3]
res = Insertionsort(A)
print(res)
