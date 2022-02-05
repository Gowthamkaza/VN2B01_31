'''
student name,id,annaual income of father



below 1 lak eligible for fee reimbursement
above 1 lak not eligible for fee reimbursement
'''

class Student:
    def __init__(self,std_name,std_id,std_F_anl_income):

        self.std_name=std_name
        self.std_id=std_id
        self.std_F_anl_income=std_F_anl_income

    def get_student_details(self):
        print("student details",self.std_name,self.std_id,self.std_F_anl_income)

    def Income(self,std_F_anl_income):

        if std_F_anl_income>0 and std_F_anl_income<=100000:
            print("the student is eligible for fee reimbursement")
        else:
            print("the student is not eligible for fee reimbursement")
obj=Student('uday',23,100000)
y=obj.std_F_anl_income
obj.Income(y)
obj.get_student_details()
obj.Income(250000)

print("----------------------------------")


#instant variable,class variable

#instant variable creation
biket='champion1'
brandts='hercules'

class Cycle:
    high = '20000'
    mid =10000
    low =5000
    def __init__(self,b_name,b_model,speed):
        self.b_name=b_name
        self.b_model=b_model
        self.speed=speed
    def get_bike_details(self):
        print("bike details",self.b_name,self.b_model,self.speed,Cycle.high,Cycle.mid,Cycle.low)

    @classmethod
    def bike_cost(cls):
        print("bike cost is",cls.high,cls.mid,cls.low)



obj23=Cycle('hero',23456,'200rmp')
obj23.get_bike_details()
obj24=Cycle('22000','14000','4000')
obj24.get_bike_details()
obj24.bike_cost()

print("----------------------------------")
Cycle.bike_cost()





class Grocories:
    Food = "fruits"
    f2 = "vegetables"

    def __init__(self,market_items,organic_items):
        self.market=market_items
        self.organic_items=organic_items
    def get_grocery_dtls(self):
        print("grocery details",self.market,self.organic_items)

    @classmethod
    def get_new_items(cls):
         print("add new items" ,cls.Food,cls.f2)
        










