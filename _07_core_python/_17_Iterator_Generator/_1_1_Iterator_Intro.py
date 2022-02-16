# https://www.programiz.com/python-programming/iterator

# EVERYTHING IS AN OBJECT IN PYTHON

li = list()   # list([])  Employee(10,'Madhu')
print("Empty list : ", li)

li = []       # list([])
print("Empty list : ", li)


list1 = [1, 2, 3, 4]  # list1 = list( [1,2,3,4] )
print("before updating: ",id(list1[2]))
list1[2] = 22
print("after updating: ",id(list1[2]))
# Iterator Mechanism
for each in list1:
    print(each)
print("Outside for loop")

print("-----------range-----------------")
for each in range(10):
    print(each)

print("-----------list1----------------")
list1 = [1, 2, 3, 4]

for each in list1:  # list1.__iter__()  ==> itr.__next__
    print(each)
'''
Step 1. On list object list1, __iter__() / iter() method will be called.
        list1.iter()  or list1.__iter__() 
        We will get iterator object    
        
Step2 : On iterator object, __next__() / next()  method will be called,
       so that we will get elements one by one in sequence.
'''

'''
__iter__()  - iter()
__next__()  - next()

list1              ==> iterable object
list1.__iter__()   ==> iterator   
iterator.__next__() => one element at a time
'''
'''
Python Iterators :
Iterators are objects that can be iterated upon. 
Let us see how iterator works and how you can build your own iterator using __iter__ and __next__ methods.

1.What are iterators in Python?
==================================
  => Iterator in Python is simply an object that can be iterated upon. 
     An object which will return data, one element at a time.
  => Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators 
  etc. but hidden in plain sight.
  => Technically speaking, Python iterator object must implement two special methods, 
                  __iter__() and 
                  __next__(), 
                  collectively called the iterator protocol.
  => An object is called iterable if we can get an iterator from it. 
     Most of built-in containers in Python like: list, tuple, string etc. are iterables.
  => iter() function (which in turn calls the __iter__() method) returns an iterator from them.

2. Iterating Through an Iterator in Python
==========================================
  => We use the next() function to manually iterate through all the items of an iterator. 
     When we reach the end and there is no more data to be returned, it will raise StopIteration
'''
print('---------Iterator For loop Mechanism-----------')
my_list = [4, 7, 0, 3]
print(my_list)         # my_list.__str__()
for each in my_list:
    print(each)

my_list = [4, 7, 0, 3]        # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__())  # Exception occurs
''''''
print("---------Iterator Internal Mechanism-----------")

try:
    print(my_iter.__next__())  # 3. Iterate through it using __next()__
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())
    print(my_iter.__next__())     # This will raise exception, as no items left in my_list
except StopIteration as si:

    print("Stopping iterations")
'''

3. How for loop actually works?
  => As we see in the above example, the for loop was able to iterate automatically through the list.
  => In fact the for loop can iterate over any iterable. 
     Let's take a closer look at how the for loop is actually implemented in Python.
     
  for element in iterable:
    # do something with element
                                       Is actually implemented as.


iter_obj = iter(iterable)            # create an iterator object from that iterable

while True:                          # infinite loop
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
        
    So internally, the for loop creates an iterator object, iter_obj by calling iter() on the iterable.

Ironically, this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. 
After all the items exhaust, StopIteration is raised which is internally caught and the loop ends. 
Note that any other kind of exception will pass through.
'''

'''
4. Building Your Own Iterator in Python
    => Building an iterator from scratch is easy in Python. 
       We just have to implement the methods __iter__() and __next__().
    => The __iter__() method returns the iterator object itself. 
       If required, some initialization can be performed.
    => The __next__() method must return the next item in the sequence. 
       On reaching the end, and in subsequent calls, it must raise StopIteration.
'''
'''

Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets. 
The iterator object is initialized using the iter() method. It uses the next() method for iteration.
 

__iter(iterable)__ method that is called for the initialization of an iterator. This returns an iterator object
next ( __next__ in Python 3) The next method returns the next value for the iterable. 
When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an 
iterator object which further uses next() method to iterate over. 
This method raises a StopIteration to signal the end of the iteration.

# example of a python inbuilt iterator
# value can be anything which can be iterate
'''
iterable_value = 'MONEY'
iterable_obj = iter(iterable_value)

while True:
    try:

        # Iterate by calling next
        item = next(iterable_obj)
        print(item)
    except StopIteration:

        # exception will happen when iteration will over
        break

'''
Below is a simple Python custom iterator that creates iterator type that iterates from 10 to a given limit. 
For example, if the limit is 15, then it prints 10 11 12 13 14 15. And if the limit is 5, then it prints nothing.
 

# range(10,100)
# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value
'''
# An iterable user defined type
class Test:
 # Constructor
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.x = 10
        return self
    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        else:
            self.x = x + 1
            return x
 
print("_______numbers from 10 to 15___________")
for i in Test(15):
    print(i)
 
print("_________numbers upto 5____________")
for i in Test(5):
    print(i)

