class A:
    def __init__(self):
        print("This is Class A")
    def uday(self):
        print("This Method Of Class A")
    def Gowtham(self):
        print("This Is Gowtham met Of Class ggggg A")

class B:

   # def __init__(self):
       # print("This is Class B")
    def Gowtham(self):
        print("This Is Gowtham met Of Class B")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("This Is Class C(A,B)")
    def Basi(self):
        print("This is Basi Met Of Class C(A,B)")
        super().Gowtham()
        super().uday()

obj = C()
#obj.Gowtham()
#obj.uday()
obj.Basi()

