x=int(input("entrt the cost of bike price:"))
if x>100000:
    print("the tax is 15",x*0.15)
elif x<=100000 and x>50000:
    print("the tax is 10","%",x*0.10)
else:
    print("the tax amount is 5",x*0.05)





