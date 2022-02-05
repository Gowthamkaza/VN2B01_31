'''
"Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

used to store data values like a map, which, unlike other Data Types that hold only a single value as an element,

Dictionary holds key:value pair. Key-value is provided in the dictionary to make
it more optimized."
'''
# Immutable: int float bool string tuple
# Mutable  : list, dict, set
x={"emp_id":21,
   'name':'gowtham',
   'loc': 'bangalore',
   'pin': 560037,
   'address':{'house_no':156,'area':'kundanahalli'}
}
print(x)
print(x['loc'])
print(x['pin'])
print(x['address'])
print(x['address']['area'])
print(x['address']['house_no'])

print(x.items())
for key,val in x.items():
   print(key,"----",val)

'''
Dictionary : 
    - Mutable data structure
    - Unordered
    - Key value pair i.e, item 
    Key properties:
        - Keys must be UNIQUE
        - Keys must be IMMUTABLE and values can be anything

'''
# 1. Keys must be IMMUTABLE and values can be anything

dict1 = {100: 10,
         200: {1: 1, 2: 2},
         102.3: 29,
         True: 'ravi',
         'Message': [1, 2, 3, 4, 5],
         (1, 2, 3): (1, 2, 3),
         # [1,2,3] : {1:1,2:2},  # Wrong, List is mutable
         # {1:1,2:2} : "Hello"   # Wrong, dict is mutable
         # {1,2,3} : "Hello"     # Wrong, set is mutable
         }
print("Keys immutable : ", dict1)
# Dict keys should not be List, Dictionary, Set


order_details = {'order_no': 145683,
                 'ref_no': 34582,
                 'cust_name': 'Gowtham',
                 'del_loc': 'Bangalore',
                 'total_bill': 1000.56,
                 'discount': 200,
                 'disc_percnt': 5,
                 'pin_code': 560037,
                 'no_of_items': 4,
                 }
print(order_details )
for key,val in order_details.items():
   print(key,'---',val)

print(order_details["discount"])


#list, set,dic are mutable so we can't use them in values of keys.
#int, string and float are immutable so we can use them.


# 2. Keys must be unique
x = 30
x = 50

dict25 = {30: 100,
         50: 100,

         }
print("Keys must be unique :", dict25)


# Dictionary is mutable

# CREATE
dat= {1: 'One', 2: 'Two', 3: 'Three', 'id': '100'}
# RETRIEVE
print('dictionary:',dat)
print('dictionary item',dat[3])
print("Dict item  :", dat['id'])

# UPDATE
dat= {1: 'One', 2: 'Two', 3: 'Three', 'id': '100'}
dat[2] = 'Twenty'
dat['id'] = 200
print("Dictionary update: ", dat)

# DELETE
del dat[1]
del dat['id']
print(dat)

dat.clear()
print("dictionary delete",dat)

x = 10
print("X : ", x)
del x
print(dat)

#dictionary functions

# len()
data3 = {'eid': 24,
          'name': 'Ram',
          'sal': 140000,
          'mobile': '6302402929',
          'office': 'Bangalore'
          }

print("Length of dict : ", len(data3))

# type()
print("Type of dict : ", type(data3))

# str()
di_str = str(data3)
print("Dict in string format :", type(di_str), di_str)





# Builtin functions:
#=======================
e_data = {'eid': 100,
          'name': 'MadhuN',
          'sal': 14000,
          'mobile': '7406900500',
          'office': 'Bangalore'
          }

# 1. keys() :To retrieve all keys from dictionary
print("-----------1. KEYS----------")
d_keys=e_data.keys()
d_val=e_data.values()
print("E data keys",d_keys,type(d_keys))
print("-----Dictionary keys ------")
for key in e_data.keys():   # list(e_data.keys())
    print(key)


# values() : To retrieve all values from dictionary
print("E data values",d_val,type(d_val))

print("-----Dictionary values ------")
for val in e_data.values():  # list(e_data.values())
    print(val)

print("-----------3. items() ----------")
# 3. items() : To retrieve all items from dictionary
items = e_data.items()
print("E DATA Items : ", items, type(items))
items = list(items) # [('eid', 100), ('name', 'MadhuN') .... ]
print("E DATA Items : ", items, type(items))


n1, n2 = (1, 2)  # tuple unpacking
print("Values : ", n1, n2)
print("iterating thorugh dictionart items")
for item in e_data.items():
    print(item)


# 4. update()
print("-----------4. update() ----------")
list1 = [1, 2, 3]
list2 = [4, 5, 6]  # [1,2,3,4,5,6]
list1.extend(list2)
print(list1)
list2.extend(list1)

x={1:5,6:5,7:8}
y={8:8,9:0,5:7}
x.update(y)
print(x)
for keys,values in x.items():
    print(keys,":",values)


print("-----------5. clear() ----------")
j = {1: 1, 2: 2, 3: 3, 4: 4}
print("Before clear : ", j)
j.clear()
print("After clear : ", j)

di = {1: 1, 2: 2}
di = di.fromkeys([10, 20, 30, 40], "Hello")

print("Dictionary from keys : ", di)

print("-----------7. copy() ----------")
di1 = {1: 1, 2: 2}
di2 = di1.copy()

print("Dict1 copy : ", di1)
print("Dict2 copy : ", di2)

#pop---Removes the element with the specified key

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")
print("Pop element",car)

#pop-item---Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print("Pop item",car)

e_data = {'eid': 568,
          'name': 'krishna',
          'sal': 150000,
          'mobile': '8978695243',
          'office': 'Bangalore'
          }
print(e_data)
print(e_data.get('sal'))


