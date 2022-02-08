
x = 175

'''
        Write Operation
1. First  python will load the statement
2. Start the execution from RHS to LHS
3. RHS : Finds the data type of given value . Here the data type of given value is INTEGER
4. If there is any operation in the given value it performs the operation.
   Here there is no operation, so it directly converts the given value into binary code.
   The binary code of given value is   1 0 1 0 1 1 1 1
5. Now the memory will locate a address for binary value.
6. The locatedmemory address will given to variable x

'''
print(x)
print(id(x))
print(type(x))

'''
            Read Operation
1. First python will go the variable referred Memory address.
2. It will load the binary value of that referred address.
3. Converts the binary  value into decimal value.
4. Gives(Prints) the value to console.
'''

d= False
print(id(d),type(d))

y = z = 150
print(y,z,id(y),id(z))
print(y is not z)
a = 30
b = a
print(a,b,id(a),id(b))
