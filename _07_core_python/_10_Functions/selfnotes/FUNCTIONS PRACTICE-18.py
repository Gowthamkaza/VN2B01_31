# call function with 3 arguments
#func1(20, 40, 60)
#Return multiple values from a function


def func(*args):
    for i in args:
        print(i)

func(20,40,60)
func(80,100)

'''
Write a program to create function calculation() such that it can accept two variables and 
calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

res = calculation(40, 10)
'''
def calculation(n1,n2):
    x=n1+n2
    y=n1-n2
    return x,y
res=calculation(40,10)
print("problem 2 result",res)

#Create a function with default argument
'''
Write a program to create a function show_employee() using the following conditions.
It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary
'''
def show_employee(name,salary=9000):
    print("name:",name,"salary:",salary)

show_employee("raghav",15000)
show_employee("raju")

'''Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it'''

def outer_func(a,b):
     def addition(a,b):
        return a+b

     add=addition(a,b)
     return add + 5

result=outer_func(5,10)
print(result)

#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10
def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
res = addition(10)
print(res)
res2=addition(20)
print(res2)


#Below is the function display_student(name, age). Assign a new name show_student(name, age)
# to it and call it using the new name.
def display_student(name,age):
    print(name,age)

display_student("ranjith",26)
show_student=display_student

show_student("ranjith",26)

#global variable and local variable

def fun():
    global employee
    employee = "santosh"
    print(employee)
fun()
print(employee)


def fruits():
    global fruit
    fruit="straw_berry"
    print(fruit)
fruits()
print(fruit)


#finding length of given string
details="python worlds"
def h3(details):
    len=0
    for char in details:
        len+=1
    print("length of given string",len)
h3(details)  #it includes white spaces also


#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

g5=lambda a,b,c:a+b+c
print(g5(5,8,9))

# Find square of given value 6
val=int(input("enter value:"))

def func_square(E_no):
    res=E_no*E_no
    return res
sq_val=func_square(val)
print("print square value",sq_val)

x=150
print("value of x",x)

def get_data():
    x=45
    print("value of x",x)

get_data()


def employee(x1,x2):
    z2=x1+x2
    f2=x1-x2
    return z2,f2
result = employee(5,10)

print(result)
