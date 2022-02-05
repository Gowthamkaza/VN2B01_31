
'''

If rating is 4 to 5 - 30%
             3 to 4 - 20%
             2 to 3 - 10%
             <2     -  no hike
'''

class Employee:
    def __init__(self,eid,name,salary):
        print(self)
        self.eid=eid
        self.name=name
        self.sal=salary

        print("employ information",self.eid,self.name,self.sal)
    def get_emp_details(self):
        print("employ information",self.eid,self.name,self.sal)

    def apply_hike(self, rating):
        print("Employee hike with rating : ", rating)
        if rating >= 4 and rating <= 5:
            hike = self.sal*30/100
            print(" Hike is :: ", hike)
        elif rating >= 3 and rating < 4:
            hike = self.sal*20/100
            print(" Hike is :: ", hike)
        elif rating >= 2 and rating < 3:
            hike = self.sal*10/100
            print(" Hike is :: ", hike)
        else:
            print(" Hike is :: ", 0)

x = Employee(12, 'Gowtham', 50000)
Employee.get_emp_details(x)
val = int(input("Please enter rating: "))
Employee.apply_hike(x, val)

x.get_emp_details()
x.apply_hike(val)





