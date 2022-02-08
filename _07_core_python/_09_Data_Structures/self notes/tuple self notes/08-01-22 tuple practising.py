list1= [1, 2, 3, 4]     # Mutable
tup1 = (1, 2, 3, 4)    # Immutable
print(tup1, type(tup1))


tuple1=()
print("empty tuple known:",tuple1, type(tuple1))
tuple2=("hello")
print("tuple with string",tuple2,type(tuple2))
tuple3=(5,)
print("tuple with int",tuple3,type(tuple3))

#Indexing
tuple4 = (1, 2, 3, 4, 5, 6, 7)
print("Indexing : ", tuple4[5])

# Slicing
print("Slicing : ", tuple4[2:5])

# Adding
t1 = (1, 5, 8)
t2 = (4, 5, 6)
print("Tuple5 : ", t1)
print("Adding : ", t1 + t2)
t1 = t1 + t2
print("Tuple6 : ", t1)

# Multiplying
t1 = (1, 2, 3)
print("Mulitiplye : ", t1*4)
# Membership
t1 = ( 2, 3, 4,5,6,56)
print("Membership : ", 1 in t1)
print("Length : ", len(t1))
print("Max : ", max(t1))
print("Min : ", min(t1))

#tuple is immutable .so we can't use the append function directly.
t7=(1,5,8,9,[7,8,9])
t7[4].append(200)
print("using list in tuple with append function:",t7)

t8 = (10, 43, 2, 532, 53, 64, 24, 25, 53)
print("Iterate the tuple")             #iteration means for taking each item of something, one after another
for k in t8:
    print(k)

t9=(1,2,5,89,56,45,232,56,84,78)
t10=len(t9)
for i in range(t10):
    print(i,":",t9[i])

#index of 89
t11=(1,56,89,48,78,75,65,89)
t12=len(t11)
print("length of t11",t12)
for i in range(len(t11)):
    if t11[i]==78:
        print("index is :",i)


t13=(1,56,89,48,78,75,65,89,96,89,78)
t13.count(89)
print("count :",t13.count(89))
print("index:",t13.index(65))

t14=[4,5,6]
t14.append(10)
print("append",t14)

print("pop",t14.pop(1))   #it calculates by indexing number
#remove
t15=t14.remove(6)
print("Remove:",t14)















