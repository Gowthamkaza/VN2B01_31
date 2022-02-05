# if statement
# if statemnet usnig arthematic operators

c=20
b=34
if(c+b):
    print("result",c+b)

a=50
b=70
if(a-b):
    print("result",a-b)
h=100
j=500
if(h*j):
    print("result",h*j)

g=50
n=10
if(g/n):
    print("result",g/n)

aravind = "photographer"
if (aravind == "photographer"):
    print("master of photography")
# if stataement using relational operators
x = 10
y = 20
z = (x + y)
print(z)
if (z == (x + y)):
    print("z value is true")

x = 10
y = 20
if x < y:
    print('y is greater than x')

x = 30
y = 20
if x < y:
    print('y is less than x')
# the above line is not executed , beacuse of x is greater than y

x = 90
y = 60
if x > y:
    print('x is greater than y')

x = 30
y = 30
if x == y:
    print('x and y are same')
x = 30
y = 50
if x != y:
    print('x and y are not equal')
x = 30
y = 32
if x <= y:
    print('x is lessthan or equal to y')
x = 50
y = 25
if x >= y:
    print('x is greaterthan or equal to y')

a = 20
c = 500
if c > a:
  print('c is greater than a')
# if we are not giving the space before print then it will show us the indentationerror

#now we are using if else condition
a = 500
b = 200
if a < b:
    print('b is greater than a')
else:
    print("a is greater than b")