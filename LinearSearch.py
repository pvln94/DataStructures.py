# This Algorithm doesn't check whether list is sorted or not as Binary search. Applicable for any type of list.

# Algorithm
# LinearSearch(list,key)
#     for each item in list
#         if item = K 
#             return its index

def LinearSearch(array,n,x):
    for i in range(0,n):
        if array[i] == x:
            return i
    return -1    

A = [1,2,3,4,5]
n = len(A)
x = 4
res = LinearSearch(A,n,x)
if res == -1:
    print("Element is not in array")
else:
        print(res)