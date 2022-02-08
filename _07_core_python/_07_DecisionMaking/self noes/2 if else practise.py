# if else statement

c=20
b=34
if(c+b):
    print("result",c+b)

a=50
b=70
if(a-b):
    print("result",a-b)
elif(a-b):
    print("result",a-b)


x = 10
y = 20
if x < y:
    print('y is greater than x')

x = 30
y = 20
if x < y:
    print('y is less than x')
else :
    print("x is greater than y")

x = 30
y = 30
if x == y:
    print('x and y are same')
x = 30
y = 50
if x <= y:
    print('x is lessthan or equal to y')
else:
    print('y is greater than or equal to x')

x = 50
y = 25
if x >= y:
    print('x is greaterthan or equal to y')
else:
    print('x is greater than or equal to y')
'''Find Student result for input marks with class category. 
                    First class  >= 60
                    Second class >= 50 and < 60
                    Third class  >= 35 and < 50
'''
a=(int(input("enter marks:")))
if a >= 60 :
    print("Result :First class")
elif a >= 50 and a < 60 :
    print("Result: second class")
elif a >= 35 and a < 50 :
    print("Result: Third class")
else:
    print("Result :fail")
b=int(input("enter marks:"))
if b>=60:
  print("Result :First class")
elif b >= 50 and b < 60 :
    print("Result: second class")
elif b >= 35 and b < 50 :
    print("Result: Third class")
else:
    print("Result :fail")

c=int(input("enter marks:"))
if c>=60:
  print("Result :First class")
elif c >= 50 and c < 60 :
    print("Result: second class")
elif c >= 35 and c < 50 :
    print("Result: Third class")
else:
    print("Result :fail")



a=int(input("enter marks"))

