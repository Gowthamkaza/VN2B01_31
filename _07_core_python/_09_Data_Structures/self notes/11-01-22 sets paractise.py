#Sets

# Creating a set
# A set is created by using the set() function or placing all the elements
# within a pair of curly braces.{}

x=set([1,2,3,4])   #list conversion of set
y={'ravi','kiran','raghu'}
z={5,'kiran',True}
print(x)
print(y)
print(z)
# the result of the set is unordered

# add()	Adds an element to the set
y.add('ramesh')
print("using the  add():", y)
y.add('ravi')
print(y)        #set does not allow duplicates

#clear()	Removes all the elements from the set
y.clear()
print("using the clear():",y)

#pop() Removes an element from the set
h1={'clock','table','pen','pencil'}
h8=h1.pop()    #here it removes the element randomly
print("pop",h8)

#discard()	Remove the specified item
h1={'clock','table','pen','pencil'}
print("before discard",h1)
h1.discard("pen")
print('after discard:',h1)



#union of sets()	Return a set containing the union of sets
h2={'clock','table','pen','pencil'}
h3={'table','chair','phone','box','pencil'}
result=h2.union(h3)
print('union of sets:',result)
result1=h2|h3   #union by using by the symbol "|"
print(result1)


#intersection()	Returns a set, that is the intersection of two or more sets
h2={'clock','table','pen','pencil'}
h3={'table','chair','phone','box','pencil'}
'''result=h2.intersection(h3)
print('intersection of sets:',result)'''

result=h2&h3        #intersection using by the symbol "&"
print('intersection of sets:',result)

#difference()	Returns a set containing the difference between two or more sets

# Return a set that contains the items that only exist in set a1, and not in set b1:
a1={"python","java",".net",'php'}
b1={"python","html","css",".net","colab"}
'''
result3=a1.difference(b1)
print("difference of sets:",result3)
'''
result4=a1-b1       # difference using by the symbol "-"
print("difference of sets:",result4)
#like wise  when we use b-a it gives only the values containing in b only
result5=b1-a1
print("difference of sets:",result5)

#comparision sets
#subset
#issubset()	Returns whether another set contains this set or not
# the symbol of subset is <=
set1={'jan','feb','mar','apr','may','jun'}
set2={'jan','feb','mar','apr','may','jun','aug','sep','nov'}
'''
result6=set1.issubset(set2)
print("subset:",result6)
'''
result7=set1<=set2          #using the symbol of <=
print("subset:",result7)

#super set
#issuperset()	Returns whether this set contains another set or not
# the symbol of subset is >=
set1={'jan','feb','mar','apr','may','jun'}
set2={'jan','feb','mar','apr','may','jun','aug','sep','nov'}
'''
result8=set2.issuperset(set1)
print("super set",result8)
'''
result9=set2>=set1
print("super set",result9)








