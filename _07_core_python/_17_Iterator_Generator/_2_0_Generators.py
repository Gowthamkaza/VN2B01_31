
# https://www.programiz.com/python-programming/generator#:~:text=Python%20generators%20are%20a%20simple,one%20value%20at%20a%20time).
# https://www.programiz.com/python-programming/generator
'''
Python 2.x
--------------
range  - Iterator   -- Speed of execution
xrange - Generator  -- Memory management
    
Python 3.x 
-----------
range  - Generator

What are generators in Python?
 => There is a lot of overhead in building an iterator in Python
    We have to implement a class with __iter__() and __next__() method,
    keep track of internal states,raise StopIteration when there was no values to be returned etc.
    This is both lengthy and counter intuitive.
  
 => Generator comes into rescue in such situations.
 => Python generators are a simple way of creating iterators
     All the overhead we mentioned above are automatically handled by generators in Python.
=> A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

How to create a generator in Python?

=> It is fairly simple to create a generator in Python. 
=> It is as easy as defining a normal function with yield statement instead of a return statement.

=> If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. 
   Both yield and return will return some value from a function.

=> The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and 
   later continues from there on successive calls.
'''
'''
Generators in Python :
=======================
There is a lot of work in building an iterator in Python. 
We have to implement a class with __iter__() and __next__() 
method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counter intuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. 
All the work we mentioned above are automatically handled by  generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over 
(one value at a time).
'''
'''
1. Generator function
2. Generator object


Generator-Function : A generator-function is defined like a normal function, but whenever 
it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function.

# A generator function that yields 1 for first time,
# 2 second time and 3 third time
'''
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

'''
Generator-Object : Generator functions return a generator object. Generator objects are used 
either by calling the next method on the generator object or using the generator object 
in a “for in” loop 

# A Python program to demonstrate use of 
# generator object with next() 
'''
# A generator function
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
   
# x is a generator object
x = simpleGeneratorFun()
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
'''
So a generator function returns an generator object that is iterable, i.e., 
can be used as an Iterators .

As another example, below is a generator for Fibonacci Numbers.

'''
# A simple generator for Fibonacci Numbers
def fib(limit):

    # Initialize first two Fibonacci Numbers 
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
  
# Create a generator object
x = fib(5)
  
# Iterating over the generator object using next
print(x.next()) # In Python 3, __next__()
print(x.next())
print(x.next())
print(x.next())
print(x.next())
  
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5): 
    print(i)



#Applications : Suppose we to create a stream of Fibonacci numbers, adopting the generator approach makes it trivial;
# we just have to call next(x) to get the next Fibonacci number without bothering about where or
# when the stream of numbers ends.
# A more practical type of stream processing is handling large data files such as log files.
# Generators provide a space efficient method for such data processing as only parts of the file are handled
# at one given point in time. We can also use Iterators for these purposes,
# but Generator provides a quick way (We don’t need to write __next__ and __iter__ methods here).



