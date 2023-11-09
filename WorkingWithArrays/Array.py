#For creating an array in python we have to Import array module.
import array as myarray
import numpy as np
# #This is how we create an array
arr= myarray.array('i',[1,2,3,4,5,6])
#TO get the type codes
print(arr.typecode)
#TO get the length of an array
print(len(arr))
#To print all the elments in the array
for i in range (0,len(arr)):
    print(arr[i],end= " ")
#How to get an array of 100 numbers.
x=list(range(1,100))
new_arr=myarray.array('i',x)
for i in range (0,len(new_arr)):
    print(new_arr[i], end=",")
#How to add an element to an array.
#There are two ways one is appen and the other is insert through insert we can pass the index where we want to add
#and through appen the elment goes and joins at the end.
arr.insert(0,12)
print(arr)
arr.append(40)
print(arr)
#How to update an array.
arr[2]= 10
print(arr)
#How to deleat an element.
#pop works with index values.
arr.pop(3)
#Remove works with the value in the array
arr.remove(5)
print(arr)
#sliceing in array.
#This slices the array from 10 index to 20 index.
arr1 = new_arr[10:20]
print(arr1)
# This slices the value from 10 to till the last 80th element.
arr2 = new_arr[10:-80]
print(arr2)
#This is used to reverse the array.
arr3= new_arr[::-1]
print(arr3)
# #Searching of an element index
ind = new_arr.index(99)
res= new_arr[ind]
print(ind,res)
# Sorting an array.
arr10=myarray.array('i',[2,3,4,9,6,7,3,5,1])
arrsort = arr10.tolist()
#Sorting an array in decending order.
arrsort.sort(reverse=True)
print(arrsort)
#numpy arrays
#creating numpy arrays
import numpy as np
arr = np.array([1,2,3,4,5])
print (arr)
print ("\n")
#creating an array with all zeros
zeros = np.zeros ((2,2))
#creatIng an array with all ones
ones = np.ones((2,2))
#creating an array with constant values
const = np.full((3,3), 10)
#creating an identity matrix
iden = np.eye(4)
#creating an array with random values
rndom = np. random.random((2,3))
print (zeros)
print ("\n")
print (ones)
print(iden)
print("\n")
print(rndom)

