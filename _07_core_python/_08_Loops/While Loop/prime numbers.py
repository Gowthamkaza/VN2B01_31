

x = int(input("Enter number: "))
if x > 1:
   for i in range(2, x):
      if (x % i) == 0:
         print(x, "is not a prime number")
         print(i, "times", x // i, "is", x)
         break
   else:
      print(x, "is a prime number")
else:
   print(x, "is not a prime number")



lower = int(input("Enter the lower value:"))
upper = int(input("Enter the upper value:"))
for number in range(lower,upper+1):
    if number>1:
        for i in range(2,number):
            if (number % i)==0:
                break
        else:
            print(number)


