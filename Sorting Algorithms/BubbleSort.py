# Algorithm
# bubblesort(array)
#  for i = 1 to indexoflastunsortedelement - 1
#     if left > right
#         swap left and right elements
#  end bubblesort      

def bubblesort(array):
    # i for iteration
    for i in range(len(array)):
        # j for every element in array
        for j in range(len(array)-i-1): # this line have len-i-1, this is for when we had completed one iteration then last will be the greater element among all. so we will not include that element again in the next iteration.
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array            
A = [2,4,1,6,3]
res = bubblesort(A)
print(res)                
