'''
Python RegEx
===============
In Python, one could easily check the presence of a text string within another string.
But, in some scenarios, we may not have the exact text to match.

For example, what if you want to check whether any valid email address is present.
This is where regular expression plays its part.


Regular Expressions
Basic Regular Expressions
Compiled Regular Expressions

1.Regular Expressions:
=====================
A regular expression is a powerful tool for matching text, based on a pre-defined pattern.
It can detect the presence or absence of a text by matching with a particular pattern, and also can split
a pattern into one or more sub-patterns.
The Python standard library provides a "re" module for regular expressions.
Its primary function is to offer a search, where it takes a regular expression and a string.
Here, it either returns the first match or else none.

'''
import re


match = re.search(r'portal', ' A computer science \
                  portal for geeks')
print(match)
print(match.group())

print('Start Index:', match.start())
print('End Index:', match.end())

'''
r character (r’portal’) -------> stands raw, not regex 

The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. 
This is because the regular expression engine uses \ character for its own escaping purpose.

The group method returns the matching string, and the start and end method provides the starting and ending string index. 
Apart from this, it has so many other methods, which we will discuss later.


Advantage of Regular expression:
=================================
Data Mining:
============
Regular expression is the best tool for data mining. It efficiently identifies a text 
in a heap of text by checking with a pre-defined pattern. 
Some common scenarios are identifying an email, URL, or phone from a pile of text.

Data Validation: 
=================
Regular expression can perfectly validate data. It can include a wide array of validation processes by 
defining different sets of patterns. A few examples are validating phone numbers, emails, etc.


Basic Regular Expressions
=========================
Let’s understand some of the basic regular expressions. They are as follows:

Character Classes
Rangers
Negation
Shortcuts
Beginning and End of String
Any Character


Character Classes:
====================
Character classes allow you to match a single set of characters with a possible set of characters. 
You can mention a character class within the square brackets. Let’s consider an example of case sensitive words. 

'''
import re


print(re.findall(r'[gG]eeks', 'GeeksforGeeks: \
                 A computer science portal for geeks'))
'''
Ranges:
=======
The range provides the flexibility to match a text with the help of a range pattern such as a 
range of numbers(0 to 9), a range of characters (A to Z), and so on. 
The hyphen character within the character class represents a range.

'''
import re

print('Range',re.search(r'[a-zA-Z0-9]', 'x'))

'''
Output
Range <_sre.SRE_Match object; span=(0, 1), match='x'>



Negation:
=========
Negation inverts a character class. It will look for a match except for the inverted character or range of 
inverted characters mentioned in the character class.

'''
import re
print(re.search(r'[^a-z]', 'c'))

'''
Output
None

In the above case, we have inverted the character class that ranges from a to z. 
If we try to match a character within the mentioned range, the regular expression engine returns None.

Let’s consider another example

'''
import re
  
print(re.search(r'G[^e]', 'Geeks'))

'''
Output
None
Here it accepts any other character that follows G, other than e.

Shortcuts:
===========
Let’s discuss some of the shortcuts provided by the regular expression engine.

\w – matches a word character
\d – matches digit character 0-9
\s – matches whitespace character (space, tab, newline, etc.)
\b – matches a zero-length character

'''
import re
  
print('Geeks:', re.search(r'\bGeeks\b', 'Geeks'))
print('GeeksforGeeks:', re.search(r'\bGeeks\b', 'GeeksforGeeks'))

'''
Output
Geeks: <_sre.SRE_Match object; span=(0, 5), match='Geeks'>
GeeksforGeeks: None



Beginning and End of String:
============================
The ^ character chooses the beginning of a string and the $ character chooses the end of a string.

'''
import re
# Beginning of String
match = re.search(r'^Geek', 'Campus Geek of the month')
print('Beg. of String:', match)
  
match = re.search(r'^Geek', 'Geek of the month')
print('Beg. of String:', match)
  
# End of String
match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks')
print('End of String:', match)

'''
Output
Beg. of String: None
Beg. of String: <_sre.SRE_Match object; span=(0, 4), match='Geek'>
End of String: <_sre.SRE_Match object; span=(31, 36), match='Geeks'>


Any Character
================
The . character represents any single character outside a bracketed character class.

'''
import re
  
print('Any Character', re.search(r'p.th.n', 'python 3'))

'''
Output
Any Character <_sre.SRE_Match object; span=(0, 6), match='python'>

'''
