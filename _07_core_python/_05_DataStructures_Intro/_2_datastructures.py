
print("------------STRING------------")
name = 'Madhu Nettem'
print(name)
print("0th index value  : ", name[0])   # indexing
print("0th index value  : ", name[6])
print("Get partial name : ", name[0:5])  # slicing

office = "Oracle India Pvt Ltd"
print(office)

# List
print("------------LIST------------")

list1 = [110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print("List1 : ", list1)
print("Index : ", list1[3])    # Indexing
print("Index : ", list1[3][2])    # Indexing
# print("Slice : ", list1[1:5])  # Slicing

# Tuple
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Madhu', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])    # Indexing
print("Index : ", tup1[3][2])    # Indexing


print("------------DICTIONARY------------")

e_data = {'eid': 100,
          'name': 'MadhuNettem',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male'
          }

print("Dict data : ", e_data)
print("Dict data : ", e_data['name'])
print("Dict data : ", e_data['sal'])


print("------------SET------------")

set1 = {1, 2, 3, 4, 5, 6}
print("Set1 : ", set1)
