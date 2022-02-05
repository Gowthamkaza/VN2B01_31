class Father:
    def fun(self,a,b):
        self.a=a
        self.b=b
        c=a+b
        return c

class Mother:
    def fun2(self,d,e):
        self.d=d
        self.e=e
        f=d*e
        return f


class child(Mother,Father):
    print("3rd class ")

obj=child()
print(obj.fun(2,5))
print(obj.fun2(5,10))
