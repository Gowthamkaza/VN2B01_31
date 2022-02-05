x=5
for i in range (x,0,-1):
    n=i
    for j in range (0,i):
        print(n,end='')
    print()
print("----------------")

#write a program to print from 1 to 20 except multiply of2&3
a=1
for a in range(1,20,):
    if a % 2==0:
        continue
    elif a % 3==0:
        continue
    else:
        a+=1
        print(a)
print()

#write a program to print the following pattern
print("-----------number pattern---------")

x=5
for i in range(0,x+1):
    n=i
    for j in range (1,i+1):
        print(j,end='')
    print()