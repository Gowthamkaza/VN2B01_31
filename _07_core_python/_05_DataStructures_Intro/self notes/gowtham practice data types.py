''' Data types :
1. Integer - 20, 1, 40, 80
2. Float - 156.29, 156.89
3. boolean- True, False
4. string - 'name', "sal", "address", "10", "100.56" , "True"

Functions
 print() - To print the given data in console
 type()  - To find the type of variable
id()    - To find variable referring address
'''

# Python program to
# demonstrate numeric value

a = 5
print("Type of a: ", type(a))     #int data type
print(id(a))

b = 5.0
print("\nType of b: ", type(b))    # float data type
print(id(b))

c = 2 + 4j
print("\nType of c: ", type(c))     # complex data type
print(id(c))

# Creating a String  with single Quotes
my_name = 'gowtham'
print(my_name)

#creating bullian data type
x=10
print (type(x))
x=bool(x)
print(type(x))
print(id(x))
del(x)
print(id(x))