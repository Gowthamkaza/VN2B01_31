
'''
the mobile phones buying price in amazon website
1)below 5,000
2)range between 5,000 to 10,000 get ---- realme3
3)range between 10,000 to 15,000    ---- samsung
4)range between 15,000 to 20,000    ---- vivo
5)range between 20,000 to 25,000    ---- one plus
6)above 25,000.                     ---- apple
'''
amount=int(input("enter your purchase mobile price:"))
if amount>=25000:
    print("select i phone models")
elif (amount >= 19999) and (amount <= 25000):
    print("select apple phones")
elif (amount >= 15000) and (amount <= 20000):
    print("select vivo phones")
elif (amount >= 10000) and (amount <= 15000):
    print("select samsung phones")
elif (amount >= 5000) and (amount <= 10000):
    print("select real me phones")
else:
    print("Hava a nice day, that amount mobile price is not available")
