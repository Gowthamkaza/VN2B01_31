#sh- for shots
#p for pants
#sht for shirts/t-shirts
sh= "shorts"
p="pants"
sht="shirts/t-shirts"
sh="x"
x=int(input("enter the amount of the  shots item"))

if x>0 and x<=100:
    print("you have no discount")
elif x>101 and x<=200:
    print("you have the discount of 5%",x*0.05)
elif x>201 and x<=300:
    print("you have the discount of 10""%",x*0.1)
else:
    print("you have the discount of 18""%",x*0.18)

print("------------")
p=int(input("enter the amount of the pants item"))
if p>0 and p<=100:
    print("you have the discount of 3""%",p*0.03)
elif p>101 and p<=200:
    print("you have the discount of 8""%",p*0.08)
elif p>201 and p<=300:
    print("you have the discount of 12""%",p*0.12)
else:
    print("you have the discount of 20""%",p*0.20)
print("---------------")

sht=int(input("enter the amount of the shirt/t-shirt item"))
if sht>0 and sht<=100:
    print("you have the discount of 5""%",sht*0.05)
elif sht>101 and sht<=200:
    print("you have the discount of 10""%",sht*0.1)
elif sht>201 and sht<=300:
    print("you have the discount of 15""%",sht*0.15)
else:
    print("you have the discount of 22""%",sht*0.22)
