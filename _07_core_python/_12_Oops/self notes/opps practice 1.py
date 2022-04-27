'''class A:
    def __init__(self,name,r_no):
        self.name=name
        self.r_no=r_no
    def get_details(self):
        print("class print:",self.name,self.r_no)

x=A(["ravi",1],['ramesh',2],)
x.get_details()
'''
# def csk(x1,x2,x3):
#     hw=x1+x2+x3
#     print(hw)
# csk(20,30,50)
# #print()
#
#
# def addvalue(a,b):
#     return a+b
# c=addvalue(10,34)
# print(c)


class Parent:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def get_details(self):
        print("Employee information:",self.name,self.id,self.salary)

c1=Parent('ravi',2,30000)
c1.get_details()

class Child(Parent):
    def __init__(self,bonus,allowance):
        super().get_details()
        self.bonus=bonus
        self.allowance=allowance
    def can3(self):
        print("other amount:",self.bonus,self.allowance)
c5=Child(20000,15000)

c5.can3()
c5.get_details()
