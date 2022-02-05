'''
OOPs Concepts
oops means- object-oriented Programming


'''
class details:
    def __init__(self,name,age):        #name,age are attributes,
        self.name=name                     # self.name here self is instance variable
        self.age=age                    # local variable is name,age

    def display(self):
        print(self.name,self.age)

r3=details('gowtham',26)            #r3 is object
r3.display()
print('---------------------')
details.display(r3)
#class example 2

class mobiles:
    def __init__(self,mobile_company,ram,camera):
        self.mobile_company=mobile_company
        self.ram=ram
        self.camera=camera

    def display(self):              #display is method name
        print(self.mobile_company,self.ram,self.camera)

p1=mobiles('vivo','4gb','16mp')
p1.display()


class games:
    def __init__(self,game_name,game_type,timing):
        self.game_name=game_name
        self.game_type=game_type
        self.timing=timing

    def view(self):
        print(self.game_name,self.game_type,self.timing)

x3=games('cricket','indoor','morning')
x3.view()




class bus:
    def __init__(self,bus_type,bus_colour):
        self.bus_type=bus_type
        self.bus_colour=bus_colour

    def tek(self):
        print(self.bus_type,self.bus_colour)


    #del

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1

print(p1)


class Person:
  pass