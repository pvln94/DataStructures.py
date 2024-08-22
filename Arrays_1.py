#1. Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
#Sample Output:
#1
#3
#5
#7
#9
#Access first three items individually
#1
#3
#5
from array import *
a=array('b',[1,3,5,7,9])
for i in range(len(a)):
    print(a[i])
print("Access first three items individually")
for i in range(3):
    print(a[i])
    


