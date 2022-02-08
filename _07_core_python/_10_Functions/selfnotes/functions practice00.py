#Python Functions
#A function is a block of code which only runs when it is called.
#A function can return data as a result.

#Calling a Function
def my_function():
    print('hello world')
my_function()

def my_function2(fname):
    print(fname + 1)

my_function2(3)

#Arguments
#Information can be passed into functions as arguments.

#Arguments are specified after the function name, inside the parentheses.

def my_function5(fname):
    print(fname+5)

my_function5(5)

def ravi(fname):
    print(fname+"sharma")

ravi("prakash")
ravi("hari")

# Number of Arguments
#By default, a function must be called with the correct number of arguments.
#Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# not more, and not less.
def uday(fname,lname):
    print(fname+ ' running ' +lname)

uday("vasanth" , "in the ground")


#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
def uday(*kid):
    print("2nd kid name is",kid[1])

uday('rakesh','harish','krishna')



