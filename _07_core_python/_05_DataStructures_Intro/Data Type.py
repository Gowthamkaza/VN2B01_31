'''
# Data types :
1. Integer - 10, 1, 20, 20
2. Float - 100.20, 128.546
3. boolean- True, False
4. string - 'name', "sal", "address", "10", "100.56" , "True"
'''

x=143
print ("\n",type(x))
print ("\n",id(x))

x=143+144-66*200/8
print ("\n",x)
print ("\nType of x:",type(x))
print ("\nid of x:", id (x))

Uday=True
print ("\nType of Uday:",type (Uday))
print ("\nId of Uday:",id (Uday))

Uday=143
print ("\nInteger:",type (Uday))

Uday=14.3
print ("\nFloat:", type (Uday))

Uday="143"
print ("\nType of Str:",type(Uday))

'''
int()
float()
complex()
bool()
'''

print("----Type conversions----")

Uday=143
print ("\nValue:",Uday,type (Uday))
# Convert to Float
Uday=float(Uday)
print ("\nValue:",Uday,type(Uday))

# Convert to Bool
Uday=bool(Uday)
print ("\nValue:",Uday,type(Uday))

