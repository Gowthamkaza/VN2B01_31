
'''prepare Algorithm for below:
1. Purchase any product in online portal
2. write a program to check whether a number is prime or not ?
'''
num=int(input("Enter any number:"))
if num >1:
    for i in range (2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"number is prime number")
else:
    print(num,"is not a prime number")











