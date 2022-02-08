'''
Inheritance:
Inheritance is defined as the capability of one class to derive or inherit the properties from
some other class and use it whenever needed.

Types of inheritance Python:
Single Inheritance: Single inheritance enables a derived class to inherit properties from a
single parent class,thus enabling code reusability and the addition of new features to existing code.
'''


class Animal:
    def __init__(self, name, b_no):
        self.name=name
        self.b_no=b_no

    def get_details(self):
        print("parent class:", self.name, self.b_no)


# obj = Animal('puppy', '3')
# obj.get_details()


class Animals2(Animal):
    def __init__(self, colour, breed, food):
        super().__init__('name', 'b_no')
        self.colour = colour
        self.breed = breed
        self.food = food

    def get_details(self):
        print("child class", self.colour, self.breed, self.food)


obj = Animals2('white', 'german_shepard', 'bones')
obj.get_details()
obj = Animal("snoopy", '1')
obj.get_details()

'''
Multiple Inheritance: When a class can be derived from more than one base class this type of
 inheritance is called multiple inheritance. In multiple inheritance, all the features of the
  base classes are inherited into the derived class. 
'''
# more than one parent class with         single child class


class Ravi:
    def __init__(self):
        print("print Ravi")


class Uday:
    def __init__(self):
        print("print Uday")


class Diviyansh:
    def __init__(self):
        print("print i")


class NickNames(Ravi, Uday, Diviyansh):
    def __init__(self):
        super().__init__()
        print("print Nick names")


s1 = NickNames()
print(NickNames.mro())

print("------------------------Multi level inheritance----------------------------")
# one super class ,one subclass and one sub subclass
class A:
    def addition(self, a, b):
        self.a = a
        self.b = b
        print("addition", a+b)


class B(A):
    def multiplication(self, a, b):
        self.a = a
        self.b = b
        print("multiplication", a*b)


class C(B):
    def subtraction(self, a, b):
        self.a = a
        self.b = b
        print("subtraction", a-b)


print("------------------addition-----------")
a1 = A()
a1.addition(5, 6)
print(A.mro())
print("------------------multiplication")
b1 = B()
b1.multiplication(7, 8)
b1.addition(21, 15)
print(B.mro())
print("------------------subtraction")
c1= C()
c1.subtraction(21, 15)
c1.addition(6, 7)
c1.multiplication(2, 8)
print(C.mro())


print("---------------------Hierarchical inheritance--------------------")
# one superclass and 2 or more subclasses


class Parents:
    def father(self):
        print("He is  father ")

    def mother(self):
        print("she is mother")


class Child1(Parents):
    def firstchild(self):
        print("i am the first child")


class Child2(Parents):
    def secondchild(self):
        print("i am the second child")


class Child3(Parents):
    def thirdchild(self):
        print("i am the third child")


print("--------------- first child---------")
obj1 = Child1()
obj1.mother()
obj1.father()
obj1.firstchild()


print("---------------2nd child------------")
obj2 = Child2()
obj2.mother()
obj2.father()
obj2.secondchild()

print("--------------- 3rd child------------")
obj3 = Child3()
obj3.mother()
obj3.father()
obj3.thirdchild()


print("---------------------Hybrid inheritance--------------------")
# Multiple types of inheritance
# in this hierarchical, multi level inheritance used

class School:
    def school(self):
        print("the school")


class Bus1(School):
    def driver1(self):
        print("he is 1 st driver of school")


class Bus2(School):
    def driver2(self):
        print("he is 2nd driver of school")


class Bus3(Bus2, Bus1):
    def driver3(self):
        print("he is 3rd driver of school")


obj = Bus3()
obj.driver1()
obj.driver2()
obj.driver3()
print(Bus3.mro())


