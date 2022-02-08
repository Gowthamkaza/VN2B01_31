
# REQ: Find square of given value

# 1mark : Find square of given value 5
print("Square of value : ", 5*5)
# 2 mark : Find square of given value 5
val = 5
print("Square of value : ", val*val)

# 5 marks : Find square of given value 5
val = int(input("Enter value : "))

def find_square(in_no):
    res = in_no * in_no
    return res

sq_val = find_square(val)
print("Square of value : ", sq_val)


# Use lambda functions  ==> map filter reduce
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

sq_val = lambda num: num * num

print("Lambda  : Square of value : ", sq_val(5))

# Covert to function
def sq_val(num):
    return num*num

print("Function : Square of value : ", sq_val(5))


# scope of variable
x = 100
print("Value of x :", x)
def get_data():
    # print("Value of x :", x)
    x = 25
    print("Value of x :", x)
get_data()
print("Value of x :", x)

# Function memory allocation
x = 10
print("x details : ", x, id(x))

def get_data():
    print("Welocome to my method")
    return "Hello World"

res = get_data()   # Function calling
print("Result is : ", res)

print("Function details ", get_data)  # Get function body address



# Mutable,Immutable :: Pass by value ,Pass by reference
# Pass by value refers to a mechanism of copying the function parameter value to another variable
# while the pass by reference refers to a mechanism of passing the actual parameters to the function.

# The main difference between pass by value and pass by reference is that,
# in a pass by value, the parameter value copies to another variable
# while, in a pass by reference, the actual parameter passes to the function.

