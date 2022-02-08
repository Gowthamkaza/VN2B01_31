# decorators practice

def div(a, b):
     print(a/b)


def smart_div(func):

     def inner(a, b):

          if a<b:
               a,b=b,a
          return func(a,b)
     return inner
div2=smart_div(div)

div2(2,4)


def func2(a,b):
     print(a/b)

def smart_func(func):
     def inner(a,b):
          if a<b:
               a,b=b,a
          return func2(a,b)
     return inner
div3=smart_func(div2)

div3(16,8)
div3(8,16)
print("assigning functions to variables")

def plus_one(number):
     return number+1

add_one=plus_one
print(add_one(5))

print("defining function inside other the function")
def plus_two(number):
     def add_two(number):
          return number +1

     result=add_two(number)
     return result
print(plus_two(6))

def plus_m(number):
    def multiply(number):
        return number*4
    result=multiply(number)
    return result
plus_m(8)
print("the multipication is:",plus_m(8))




print ("Passing Functions as Arguments to other Functions")
def plus_3(number):
     return number+1

def function_call(function):
     def add():
          number_to_add=5
          a=function('number_to_add')
          return a
     return add


function_call(plus_3)
print(plus_3(7))










