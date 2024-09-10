#python array module
import array as myarray
#creating an array
arr=myarray.array('i',[1,2,3])
arr1=myarray.array('d',[1,0,2,1,2,4,2,5,2,6])
arr2=myarray.array('u',['a','b','c','d'])
#typecodes
print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)

print(len(arr))
print(len(arr1))
print(len(arr2))

for i in range(0,len(arr)): 
    print(arr[i], end=" ")
print('\n')
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print('\n')
for i in range(0,len(arr2)):
    print(arr2[i], end=" ")
print('\n')

#Indexing
#Assessing Elements from an Array using index values
x=list(range(1,100))
new_array=myarray.array('i',x)

#printing the array
for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print('\n')
print(new_array[25])

#Adding Elements in an Array
new_arr=myarray.array('i',[3,4,5,6,7,8,9,10])
for i in range(0,len(new_arr)):
    print(new_arr[i],end=" ")
print(end=" \n")

#Adding new Elements in the array
new_arr.insert(0,2)
new_arr.insert(0,1)
#printing the new array
for i in range(0,len(new_arr)):
    print(new_arr[i],end=" ")
print('\n')

#using append
new_arr.append(15)
for i in range(0,len(new_arr)):
    print(new_arr[i], end=" ")
print('\n')

#updating elements in an array
new_array=myarray.array('i',[1,2,2,4,5])

#printing array
for i in range(0,len(new_array)):
    print(new_array[i],end=" ")
print('\n')

#updating the array
new_array[2]=3 #assignig new value at the index 2
for i in range(0, len(new_array)):
    print(new_array[i],end=" ")
print('\n')

#deleting elements in an array
new_array.pop(4)
for i in range(0, len(new_array)):
    print(new_array[i],end=" ")
print('\n')

#using the remove() method
new_array.remove(3)
for i in range(0,len(new_array)):
    print(new_array[i], end=" ")
print(end="\n")

#slicing operations in an array
x=list(range(0,100,3))
arr=myarray.array('i',x)
print(arr)
print(end="\n")

#slicing operations
arr0=arr[10:20]
for i in range(0,len(arr0)):
    print(arr0[i], end=" ")
print(end="\n")

#negative indexing
arr1=arr[10:-10]
for i in range(0,len(arr1)):
    print(arr1[i],end=" ")
print(end="\n")

#reversing the order using slicing
arr2=arr[::-1]
for i in range(0,len(arr2)):
    print(arr2[i],end=" ")

#searching operation in an array using index()
x=list(range(0,1000000,2))
search_array=myarray.array('i',x)

#print first 10 elements of the array
for i in range(0,len(search_array[0:10])):
    print(search_array[i],end=" ")
print("\n")

#search the number 10002 in the array
index=search_array.index(10002)
res=search_array[index]
print(index,res) 
 
#sorting operations
sort_array= myarray.array('i',[5,3,4,6,7,8])
sorted_array=sort_array.tolist()

#ascending order
sorted_array.sort()
print(sorted_array)

#descending order
sorted_array.sort(reverse=True)
print(sorted_array)