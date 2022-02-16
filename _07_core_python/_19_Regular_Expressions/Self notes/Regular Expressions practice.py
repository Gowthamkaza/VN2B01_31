import re

#  findall	Returns a list containing all matches

#Find all lower case characters alphabetically between "a" and "m":
#[]----- A set of characters
txt="this is Gowtham from Guntur"
x=re.findall("[a-m]",txt)
print(x)


# Signals a special sequence (can also be used to escape special characters)
import re
#    \   Signals a special sequence
txt2 = "The cost of biryani is 300 rupess"

#Find all digit characters:

x = re.findall("\d", txt2)
print(x)

import re

#   .	Any character (except newline character)
txt3 = "Metacharacters are characters with a special meaning"

#Search for a sequence that starts with "ch", followed by two (any) characters, and an "s":

x = re.findall("ch.......s", txt3)
print(x)


import re

txt4 = "hello, how are you ? "

#Check if the string starts with 'hello':
#  ^	Starts with
x = re.findall("^hello", txt4)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

import re

txt5 = "Python has a built-in package called re, which can be used to work with Regular"

#Check if the string ends with 'Regular':
#  $	Ends with

x = re.findall("Regular$", txt5)
if x:
  print("Yes, the string ends with 'Regular'")
else:
  print("No match")


import re

txt6 = "This is gowtham"

#Search for a sequence that starts with "go", followed by 0 or more  (any) characters, and an "m":
#     *     	Zero or more occurrences
x = re.findall("go.*m", txt6)
print(x)

import re

txt7 = "This is gowtham"
#+	One or more occurrences

#Search for a sequence that starts with "go", followed by 1 or more  (any) characters, and an "m":

x = re.findall("go.+m", txt7)

print(x)


#    ?	Zero or one occurrences
import re

txt8 = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt8)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


import re

txt9 = "followed excactly seven characters"
#{}	Exactly the specified number of occurrences

#Search for a sequence that starts with "ch", followed excactly 2 (any) characters, and an "s":

x = re.findall("ch.{7}s", txt9)

print(x)

import re

txt10 = "i will go to market to buy fruits!"

#Check if the string contains either "fruits" or "vegetables":

x = re.findall("fruits|vegetables", txt10)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#The search() Function
#Search for the first white-space character in the string:
import re
txt12="firsts white-space character in the string"
x12=re.search('\s',txt12)
print("the first white space character is ",x12.start())

#The split() Function
#The split() function returns a list where the string has been split at each match

import re

#Split the string at every white-space character:
txt13="the string splits by split function"
x13=re.split("\s",txt13)
print(x13)


#Split the string only at the first occurrence:
import re

txt14 = "split string coins switches also"
x = re.split("\s", txt14, 1)
print(x)






