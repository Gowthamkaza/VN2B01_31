print(",,,,...Polymorphism...,,,,")
print("          ;;;;;               ")
# Method Overloading
# Same class
# Same Function or method Name
# Different Parameters
print("......Method Overloading......")

class A:
    def sum(self, a, b ):    # This is normal
        return a * b
    def sum(self, a, b, c = 5):     # This is Overloading because of Given Perameters
        return a + b + c
obj = A()
print(obj.sum(5,6))
print()

print("2Nd Method")

class B:
    def sum(self, a, b, c = 0):
        print("Value Of Arguments :",a + b + c)
obj = B()
obj.sum(a = 20, b = 5) # # keyword args
obj.sum(5, 5, 5) ## Positional args



print()



print("////...Method Over-Riding...////")
# method Over-riding
# Different Classes
# Same methods names
# Different Perameters
class A:
    def vasu(self):
        print("This is A")
class B(A):
    def vasu(self):
        print("This is B")
        super().vasu()
class C(B):
    def vasu(self):
        print("This is C")
        super().vasu()
class D(C):
    def vasu(self):
        print("This is D")
        super().vasu()
obj = D()
obj.vasu()

class com:
    #def __init__(self):

    def config(self):
        print("15,ll,ii")
        pass












