# This Algorithm applicable only for sorted lists.

                                        # Iterative Method

# Algorithm

# do until both low and high values meet each other( use while loop)
# mid = (low+high)//2
# if x = array[mid]
#     return mid
# else if x > array[mid]
#     low = mid + 1
# else 
#     high = mid - 1    

def Iterativemethod(array,x,low,high):
    while low <= high:
        mid = (low + high)//2

        if x == array[mid]:
            return mid
        elif x > array[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

A = [1,2,3,4,5]
n = len(A)
x = 5
low = A[0]    
high = A[n-1]
res =    Iterativemethod(A,x,low,high)
if res == -1:
    print("Element is not in array")
else:
        print(res)   

                                        # Recursive Method        

# Algorithm
# BinarySearch(array,x,low,high)
    # mid = (low+high)//2
    # if x = array[mid]
    #     return mid
    # else if x > array[mid]
    #     return BinarySearch(array,x,mid + 1,high)
    # else 
    #     return BinarySearch(array,x,low,mid - 1) 

def BinarySearch(array,x,low,high):
     if low > high:
          return False
     else:
        mid = (low+high)//2
        if x == array[mid]:
              return mid
        elif x > array[mid]:
            return BinarySearch(array,x,mid + 1,high)
        else: 
            return BinarySearch(array,x,low,mid - 1) 
        
A = [1,2,3,4,5]
n = len(A)
x = 5
low = A[0]    
high = A[n-1]
res =    BinarySearch(A,x,low,high)
print(res)
            