print("Using Variables in functions")
a = "Royal"
def myfunc():
    print("My name is " + a)
myfunc()


print("Using Local Variables in functions")
b = "Charan"
def myfunc():
    b= "Lokesh"
    print("My name is " + b)
myfunc()
print("My name is " + b)


print("Changing the local Variable as global Variable using GlobalKeyword")
c = "Sai"
def myfunc():
    global c
    c= "Shiva"
    print("My name is " + c)
myfunc()
print("My name is " + c)