print("single  decorators used in one function: ")
def student(func):
    def raghav():
        func()
        print("this is ragha ")
    return raghav


@student
def ramesh():
    print("this is ramesh")

ramesh()


print("multiple decorators on one function: ")

def decorator2(func):
    def ravi():
        print("this is first step")
        func()
        print("this is 2nd step")
    return ravi

def repeat2(func):
    def gowtham():
        print('this is 4 th step')
        func()
    return gowtham


@decorator2
@repeat2
def new_func2():
    print("this is 3rd step")
new_func2()


print("----Arguments -------------")

def fun3(*args):
    print(args, "----", type(args))
    for val in args:
        print(val)
    print("the arguments")

fun3()
fun3('Hello', 'Welcome', 'to', 'python world')
fun3(1, 2, 3, 4, 5)
fun3(1, 2.4, 'Madhu', True, [1, 2, 3], (1, 2, 3), {1:1, 2:2}, {11, 2, 3})

print("sum with decorators")

def validate_nums(func):
    def wrapper(*args, **kwargs):
        if args[0] >= 0 and args[1] >= 0:
           output = func(*args, **kwargs)
           return output
        else:
             print("Please enter Positive numbers only")
    return wrapper   # wrapper(10,20)

@validate_nums
def sum(num1, num2):
    res = num1 + num2
    return res

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
result=sum(n1,n2)
print('the sum of two numbers is', result)

