course = 'python'
print(course)
i = 5

# using while loop in integer with known range
while i <= 50:
    print(i)
    i += 5

# using for loop in print the string with multiplication
print("----------------------------")
course = 'python programming'
for char in course:
    print(char)
    print(char * 10)

# using for loop in print the string
msg = "python world"
for x in msg:
    print("character:", x)

for char in 'aflkdsfdsalfsdf  324324SDFDSF@!#@!$#@%fsdfsd dsfdsFDSf!@#@!#!@':
    print(char)

# list with for loop
x = [123456, "ramesh", 25.36, True, False]
for char in x:
    print("list data:", char)

for series in [1, 2, 3, 4, 5, 6]:
    print("integers:", series)
# tuple with for loop
for exe in (1, 2, 3, 45, 56):
    print("integers:", exe)

# dictionary with for loop
#print the total dictionary
dictionary1 = {"sal": 10000, 'e_id': 123, 'name': 'gowtham'}
print(dictionary1)

#print the dictionary key values
for i in dictionary1:
    print("values:", i)
for i in dictionary1.keys():
    print('dictionary keys:', i)
#print the dictionary values/ result of them only
for i in dictionary1.values():
    print("dictionary values:",i)


#set with for loop
set={1,2,3,4,5,6}
for i in set:
    print('set values:',i)


print("-----------------for loop with strings-----------------------")
x=["ravi", "rajesh"]
for char in x:
    print("character: ",char)