'''
What is Pandas?
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created
 by Wes McKinney in 2008.

 Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science

What Can Pandas Do?
Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values.
This is called cleaning the data.
'''

#data frames
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

#Series is like a column, a DataFrame is the whole table.

# When using [], the result is a Pandas DataFrame.



import pandas
data1 = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(data1)
print(myvar)

print("creating pandas as pd")


import pandas as pd

data2 = {
  'students': ["ravi", "ramesh", "rajeev"],
  'Roll number': [5, 8, 3]
}

myvar = pd.DataFrame(data2)

print(myvar)

print("-------panda series------------")
#Pandas Series
'''
What is a Series?
A Pandas Series is like a column in a table.

It is a one-dimensional array holding data of any type.
'''

a=[1,6,8]
data3=pd.Series(a)
print(data3)
print(data3[0])
print(data3[2])



data4={
  'cellphone':['samsung','vivo','iphone','oppo'],
  'prices range':['15000','18000','45000','20000']
  }
d5=pd.DataFrame(data4)
print(d5)

d6=pd.Series(data4)
print(d6)
print(d6[1])

#changing of index numbers as labels

print("changing of index numbers as labels")

a=[1,5,8]
data7=pd.Series(a, index =['x','y','z'])
print(data7)
print("calling the created label with index value")
print(data7['y'])

#Key/Value Objects as Series
print("----Key/Value Objects as Series------")
calories={'day1':150,'day2':200,'day3':500}
data8=pd.Series(calories,index=['day1','day2'])
print(data8)

# Locate Row
#the DataFrame is like a table with rows and columns.
#Pandas use the loc attribute to return one or more specified row(s)
print("------Locate Row-------")
a=[1,6,8,7,5]
c=pd.DataFrame(a)
print(c.loc[0])
print(c.loc[[0,1]])


#Read CSV Files

#Here use to_string() to print the entire DataFrame.

import pandas as pd
f3 = pd.read_csv('AMZN.csv')
print(f3.to_string())


import pandas as pd
f3 = pd.read_csv('Stock market bokerage pricing.csv')
print(f3.to_string())