'''
Python Decorators with Examples:
-----------------------------------
Decorators are a highly effective and helpful Python feature because we can use them to
change the behavior of a function or class.
We use them to wrap another function in order to enhance its functionality without having to change it permanently.


1. Functions are Objects in Python:
=====================================
Functions are first-class objects in Python. As a result, they have all of the attributes of an object,
and we may handle them as such by assigning them to variables and passing them as arguments to other functions as arguments.

2. Assigning Functions to Variables in Python:
-------------------------------------------------

In Python, we can assign a function to a variable. We can later use that variable to call the function,

Example of assigning function to a variable
'''
def site():
    print("PythonGeeks")
website = site
print(f"{site = }")
print(f"{website = }")
site()
website()

'''
Output

site = <function site at 0x103ad7280>
website = <function site at 0x103ad7280>
PythonGeeks
PythonGeeks
In the above code example, we assigned the function site() to the variable website. 
Then we used the website variable to call the function. 
In this way, we can assign a function to as many variables as we want.

3. Passing Function as an Argument in Python:
---------------------------------------------
Similar to assigning functions to variables, we can also pass functions as arguments to other functions. 
The functions which accept the arguments are called higher-order functions.

Example of passing functions as arguments.
'''
def sqrt(num):
    return num**0.5
def square(num):
    return num**2
def math(function):
    print(function(4))
math(sqrt)
math(square)

'''
Output

2.0
16


4. Function Returning Another Function in Python
=================================================
Python also allows us to define a function that returns another function.

Example of a function returning another function in Python
'''
def str1():
    print("PythonGeeks")
def func1():
    return str1
var1 = func1()
var1()

'''
Output

PythonGeeks

5. Nested Functions in Python:
==============================
one function created within another function. These enclosed functions are called nested functions

Example of nested functions in Python
'''
def math():
    def square(num):
        return num**2
    print(square(2))
math()

'''
Output

4

6. Non-local Variable and Closure in Python
==============================================
A nested function is one that is defined inside another function. The variables of the enclosing scope 
can be accessed by nested functions. These variables are called non-local variables.

By default, non-local variables are read-only. To modify them, we need to use a keyword called nonlocal.

Closure Functions are nested functions that can access non-local variables.

Example of non-local variable and closure function in Python
'''
def math(num):
    def square():
        return num**2
    print(square())
math(2)

'''
Output
4

In the above code example, the variable num is a non-local variable. 
Although the variable num is not in the scope of the function square(), 
it still accessed it. So, the function square() is called a closure function.


Decorators in Python
=====================
Creating a Decorator in python
By using the concepts that we have learned about functions, let us create a simple decorator.

Example of creating a decorator
'''
def my_decor(func):
    def my_wrap():
        print("Decorator Function")
        return func()
    return my_wrap
'''
In the above code example, we have created a decorator called my_decor. 
Let’s have a look at how to use the above-created decorator.

Using a Decorator in Python
To use a decorator, we need to have a main function which we want to decorate and we need to assign the 
decorator function to a variable. Usually, the name of the variable must be the same as the function 
which we want to decorate.

Example of using a decorator
'''

def my_function():
    print("Main Function")
my_function = my_decor(my_function)
my_function()

'''
Output

Decorator Function
Main Function


Decorators with Arguments in Python:
=================================
We can use a decorator even when the function has some arguments. To do so we need to define our decorator a bit differently than before.

Example of decorator in Python
'''
def my_decor(func):
    def my_wrap(str1, str2):
        print("Decorator Function")
        return func(str1, str2)
    return my_wrap
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function = my_decor(my_function)
my_function("Mangoes", "Sweet")

'''
Output

Decorator Function
Main Function
Mangoes are Sweet
In the above code example, we used our decorator on a function with two arguments. 
But there is still a problem with the decorator.

The decorator only works for functions with two arguments. 
What if we wish to decorate a function with more than two arguments? Or what if we wish to decorate a function that doesn’t accept any arguments?

We can’t define different decorators for different numbers of arguments. So to resolve this, we need to use arbitrary arguments called args and kwargs.

Any number of non-keyword arguments can be passed to args, and any number of keyword arguments can be passed to kwargs. By including both of these in the decorator, we can use the decorator with any function regardless of the number of arguments.

Example of decorators in Python
'''
def my_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function")
        return func(*args, **kwargs)
    return my_wrap
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function = my_decor(my_function)
my_function("Mangoes", "Delicious")

'''
Output

Decorator Function
Main Function
Mangoes are Delicious

Using the Decorator Syntax in Python
=====================================
Python makes using decorators a lot easier. Instead of assigning the decorator to a variable, we can simply use the @ sign. This is the most common method of implementing decorators.

Example of decorator in Python
'''

def my_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function")
        return func(*args, **kwargs)
    return my_wrap
@my_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function("Mangoes", "Delicious")

'''
Output

Decorator Function
Main Function
Mangoes are Delicious


Multiple Decorators in Python
=============================
In Python, we can apply several decorators to a single function. The decorators, on the other hand, will be used in the sequence that we’ve designated. This is called chaining decorators.

Example of multiple decorators in Python
'''
def my_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function 1")
        return func(*args, **kwargs)
    return my_wrap
def my_another_decor(func):
    def my_wrap(*args, **kwargs):
        print("Decorator Function 2")
        return func(*args, **kwargs)
    return my_wrap
@my_decor
@my_another_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)
my_function("Mangoes", "Delicious")

'''
Output

Decorator Function 1
Decorator Function 2
Main Function
Mangoes are Delicious
'''