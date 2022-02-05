#encapsulation

'''
Access Modifiers in Python :
1.Public,
2.Private and
3.Protected

public - access in any where
projected - access in derived class   ‘_’ symbol
private - access only in within the class  '__'
'''

class Animal:
    def __init__(self, name, b_no):
        self.name=name
        self.b_no=b_no

    def get_details(self):
        print("normal class:",self.name,self.b_no)


# obj = Animal('puppy', '3')
# obj.get_details()


class Animals2(Animal):
    def __init__(self, colour, breed, food):
        super().__init__('name', 'b_no')
        self.colour = colour
        self.breed = breed
        self.food = food

    def get_details(self):
        print("class 2", self.colour, self.breed, self.food)


obj = Animals2('white', 'german_shepard', 'bones')
obj.get_details()
obj = Animal("snoopy", '1')
obj.get_details()
