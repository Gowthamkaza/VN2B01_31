'''
More Regular Expressions:
==========================
Some of the other regular expressions are as follows:

Optional Characters
Repetition
Shorthand
Grouping
Lookahead
Substitution


'''
print("_____Optional Characters_____")

# Regular expression engine allows you to specify optional characters using the ? character.
# It allows a character or character class either to present once or else not to occur.
# Let’s consider the example of a word with an alternative spelling – color or colour.


import re
print('Color',re.search(r'colou?r', 'color'))
print('Colour',re.search(r'colou?r', 'colour'))

'''
Output
Color <_sre.SRE_Match object; span=(0, 5), match='color'>
Colour <_sre.SRE_Match object; span=(0, 6), match='colour'>

'''
print("___________Repetition______")
# Repetition enables you to repeat the same character or character class. Consider an example of a date that consists of day, month, and year. Let’s use a regular expression to identify the date (mm-dd-yyyy).


import re
print('Date{mm-dd-yyyy}:', re.search(r'[\d]{2}-[\d]{2}-[\d]{4}',
                                     '18-08-2020'))
# Output
# Date{mm-dd-yyyy}: <_sre.SRE_Match object; span=(0, 10), match='18-08-2020'>
# Here, the regular expression engine checks for two consecutive digits. Upon finding the match, it moves to the hyphen character. After then, it checks the next two consecutive digits, and the process is repeated.


print("_____Repetition ranges___________")

# The repetition range is useful when you have to accept one or more formats. Consider a scenario where both three digits,
# as well as four digits, are accepted. Let’s have a look at the regular expression.

import re
print('Three Digit:', re.search(r'[\d]{3,4}', '189'))
print('Four Digit:', re.search(r'[\d]{3,4}', '2145'))

