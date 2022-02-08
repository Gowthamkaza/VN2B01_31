#write a program to display sum of odd numbers and even numbers that fall between 12 and 37
# (including both numbers)
a=12
for i in range  (12,38,):
    if i% 2==0:
        a=a+i
        print("even number:",i)
    else:
        print("print odd number",i)


