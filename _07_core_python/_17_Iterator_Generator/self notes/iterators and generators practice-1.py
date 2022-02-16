#iterators
num=[1,5,8,9]
'''
# using for loop
for i in num:
    print(i)
'''
it=iter(num)

#iterating the list by using next method
print(it.__next__())
print(it.__next__())
#print(it.__next__())
#print(it.__next__())

#iterating the list by using next() function
print(next(it))



#Creating a class with loop

class toptwenty:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=20:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration
#To prevent the iteration to go on forever, we can use the StopIteration statement.

values=toptwenty()

for i in values:
    print(i)


'''
a generator is a function that returns an object (iterator) which we can iterate over
#(one value at a time).
1. Generator function
2. Generator object
'''
print("-------Generator---------")
class Generator:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value
gen=Generator(10)


def gen():
    n = 1
    print('This is  first print')
    yield n
    n += 1
    print('This is second print')
    yield n
    n += 1
    print('This is final print')
    yield n

for item in gen():
    print(item)

# reverse string
print('-------reverse string----------')


def rev_str(str1):
    length = len(str1)
    for i in range(length - 1, -1, -1):
        yield str1[i]

# For loop to reverse the string
for char in rev_str("this is Gowtham"):
    print(char)



gen4 = []  #created a empty list
for letter in 'PYTHON': #iteration through sequence
   gen4.append(letter)  #appending the each element into list

print("--Using for loop----------------", gen4)

# List comprehension
gen5= [letter for letter in "python"]
print("using the list comprehension----:",gen5)

#list squaring values
values2 = [x*x for x in range(12)]
print("--Using list comprehension------", values2)

#Dictionary
vals = [1, 2, 3, 4, 5]
di={}
for each in vals:
    di[each]=each*each
print("normal for loop",di)
# Dict comprehension by for loop

di = {each: each*each for each in vals}

print("Dictionary comprehension: ", di)


#generators with maximun
def max_gen(max=0):
    n=0
    while n<max:
        yield 3**n
        n += 1

for each in max_gen(8):
    print(each)


 #Represent Infinite Stream

