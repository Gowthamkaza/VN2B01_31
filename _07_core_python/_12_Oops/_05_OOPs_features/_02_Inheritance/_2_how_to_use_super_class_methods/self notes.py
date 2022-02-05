print("-------This Is inheritance--------")
'''
# single inh

print("++++++single inh++++++")
print()
class parent:
    def Swapna(self):
        print("This is Parent Class")
class Child(parent):
    def Gow(self):
        print("This is Child Class")
obj = Child()
obj.Gow()
obj.Swapna()


# Multi Level inh
print('+++++Multi Level inh+++++')
print()

class parent:
    def Swapna(self):
        print("This is Parent Class")
class Child(parent):
    def Gow(self):
        print("This is Child Class")
class ChinnaChild(Child):
    def Simha(self):
        print("This is ChinnaChild Class")

obj = ChinnaChild()
obj.Simha() # This Is Won Function
obj.Gow() # This is Child Function
obj.Swapna() # This is parent Function

# Hierarchical inheritance (It means one parental class and two Child Class)
print("=======Hierarchical inh=======")
print()
class vn2:
    def uday(self):
        print("Vasudev")
class vn22(vn2):
    def gow(self):
        print("Uday")
class vn222(vn2):
    def Swap(self):
        print("Vasu")
obj = vn222()
obj.Swap()
obj.uday()

# Multiple inh
print("------Multiple inh------")
print()
class parent:
    def simha(self):
        print("This is parent")
class son:
    def basi(self):
        print("This is son")
class small_son(parent,son):
    def uday(self):
        print("This is small son")
obj = small_son()
obj.uday()
obj.basi()
obj.simha()


# Super inh
print("------Super inh-------")
print()
class A:
    def __init__(self):
        print("This is A")
    def uday(self):
        print("Vasudevs Nature Talk")
class B(A):
    def __init__(self):
        super().__init__()
        print("This is B")
    def vasu(self):
        print("Vasudaika Kutumbam")
obj = B()          # Because of init We are Getting this function out put
obj.vasu()
obj.uday()
'''
class A:
    def __init__(self):
        print("This is Just __Init__ Of A")
    def Uday_B (self):           # Same Fun Name
        print("This Is Uday_A")
    def Vasu_B(self):           # Same Fun Name
        print("This is Vasu_A")

class B:
    def __Uday__(self):
        print("This Is __init__ Of B")
    def Uday_A(self):           # Same Fun Name
        print("This is Uday_B")
    def Vasu_B(self):           # Same Fun Name
        print("This Is Vasu_B")

class C(A,B):
    def __init__(self):

        #super().__Uday__()

        #super().__init__()      # Method Resolution Order (MRO) => (A,B) So A Is left
        print("This is __init__ Of C(A,B)")
    def Uday_E(self):
        print("This is Uday_C(A,B)")
    def Vasu_F(self):
        print("This is Vasu_C(A,B)")

        super().Uday_A()        # It Uses IN Methods

obj = C()


#obj.Uday_A()
#obj.Vasu_B()
#obj.Vasu_F()










