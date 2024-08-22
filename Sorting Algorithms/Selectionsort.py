# This algorithm is quiet oposite to bubble sort
#Selection sort selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.

# Algorithm

# selectionSort(array, size)
#   repeat (size - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position
# end selectionSort

def Selectionsort(array,size):

    for i in range(size):
        minindex = i
        for j in range(i+1,size):
            if array[j] < array[minindex]:
                minindex = j
        (array[i],array[minindex]) =  (array[minindex],array[i])
    return array      

A = [2,1,5,3,6]
n = len(A)
res =  Selectionsort(A,n)     
print(res)       