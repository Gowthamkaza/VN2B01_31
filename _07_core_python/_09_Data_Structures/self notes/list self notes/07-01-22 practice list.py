list1 = [1, 1, 2, 3, 4, 5, 6]
print("List data structure :", list1)

list2 = [1, 4.5, True, False, (1, 2, 3), "hello", {1, 2, 3}]
print("List hetero data structure :", list2)

list3 = [10, 20, 30, 10, 20, 50]
print("list allows duplicate values:", list3)

print("----List is MUTABLE-----")
list4 = [12, 22, 13, 54, 35]
list4[3] = 500
print(list4)

print("-------------sequence operations--------------")

list5 = [1, 2, 2.56, "everything is good", True]
#  0 1  2    3                    4
print(list5[3])
print(list5[3][4])
print(list5[-1], list5[-2])

print("-------------slicing--------------")
print(list5)
print(list5[2:4])  # slicing with in range

# adding 2 lists
list6 = [1, 2, 3, 4]
list7 = [6, 7, 8]
print("adding of 2 lists", list6 + list7)
print('multiplying of 2 lists', list6 * 2)
print('multiplying of 2 lists', list7 * 2)
print('membership with a list', 3 in list6)
print('length of a list', len(list6))

# list is mutable  (mutable means we can change)
# tuple is immutable
'''# Builtin functions:
---------------------
append insert extend   : UPDATE
pop  remove            : DELETE 
count                  : RETRIEVE
index                  : RETRIEVE
reverse                : UPDATE 
sort                   : UPDATE
copy                   : CREATE
'''
# 1. append(): It appends element(any value) at end of the list
# list1.append(obj) Appends any object obj to list
list8 = [1, 5, 8, 9, 12, 56, 89]
list8.append(23)
print("after append:", list8)
list8.append(10.4)
print(list8)
list8.append(True)
print(list8)
list8.append('Hello')
print(list8)
list8.append([1, 2, 3])
print(list8)
list8.append((10, 20, 30))
print(list8)
list8.append({1: 1})
print( "after append:",list8)

# extend  : only sequence str,list,tuple
#: list1.extend(seq)         Appends the contents of seq to list
list9 = [23, 45]
list9.extend((1, 20))    #extend
print( "after extend",list9)
list10=[23, 45]
list10.append((1,20))           #append
print("after append",list10)

# 3. pop# list.pop(obj=list[-1]) Removes and returns last object
# or obj from list of our selected number
list12 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
list12.pop((5))
print(list12)
list12.pop()         #when use empty peranthisis it removes last number
print(list12)
print("--------------------")
list12 = [23, 12, 46, 34, 14, 34, 14, 7, 34, 2, 19, 25]
print(list12.pop(0))

# 4. remove
            # list.remove(obj)    Removes object obj from list
list13=[1,5,6,45,69,58,68]
list13.remove(69)
print(list13)


# 5.list.insert(index, obj)  Inserts object obj into list at offset index
list11 = [1, 2, 3, 4, 5]
print("Before index : ", list11)
list11[0] = 200  # [150, 2, 3, 4, 5]  Replace the value in index
print("After index   : ", list11)
list11.insert(0, 100)  # [100, 150, 2, 3, 4, 5] Insert the value in index
print("After insert  : ", list11)
list11.insert(3, 100)
print("After insert   : ", list11)

# 6. count ==> list.count(obj)Returns count of how many times obj occurs in list

list15=[1,12,13,12,15,26]
print(list15.count(12))

# 7. index  ==> list.index(obj) Returns the lowest index in list that obj appears
list16 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
print(list16.index(53))
print(list16.index(25))

# 8. reverse ==> list.reverse()  Reverses objects of list in place
list17 = [1, 2, 3, 4, 5]
list17.reverse()
print(list17)

# 9. sort ==> list.sort(obj)Sorts the elements
list18 = [23, 76, 23, 32, 53, 34, 25, 21, 53, 43, 16, 25, 7, 53, 13, 59]
list18.sort()      # ascending order
print(list18)
list18.sort(reverse=True)
print(list18)


# 10. copy()

list19 = [1, 2, 35, 48, 56]
list20=list19.copy()
print(list20)
list19.append(50)
print(list19)

# 2nd way of copy
list20 = [1, 2, 35, 48, 51]
list21= list20
print("Variable  copy : ", id(list20),id(list21))
list20.append(100)
print("After var copy :", list20,list21)
list21.extend([11,22])
print("After var copy :", list20,list21)


