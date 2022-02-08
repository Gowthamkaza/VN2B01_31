#Python does not have built-in support for Arrays, but Python Lists can be used instead.
#Arrays are used to store multiple values in one single variable:
'''
What is an Array?
An array is a special variable, which can hold more than one value at a time.
An array can hold many values under a single name, and you can access the values
by referring to an index number.
'''
cars = ["Ford", "Volvo", "BMW"]
print(cars)    #getting the values in the car
x = cars[0]   #getting the value of first array
print(x)
import array as arr

g3=arr.array('i',[2,4,8])
print("array1",g3)


print("---------iteration of arrays-------")
for t5 in g3:
    print(t5)

#The Length of an Array
#Use the len() method to return the length of an array (the number of elements in an array).
y=len(cars)
print("length of car:",y)


#Looping Array Elements
#we can use the for in loop to loop through all the elements of an array.
x=['yamaha','tvs','splender','glamour']
for i in x:
    print(i)

#append elements to arrays
x=['yamaha','tvs','splender','glamour']
x.append("pulsar")
print("append the elements:",x)

#pop element to arrays
x.pop(1)
print("pop element",x)
#remove element
x.remove("glamour")
print("remove element",x)

