'''
print("To print alphabhets in pyramid")

for i in range(1, 2):
    print(i, end=" ")

print("______________________")

for i in range(1, 3):
    print(i, end=" ")

print("______________________")
'''

for i in range(1, 5):
    for j in range(1,i):
        print(j,end=' ')
    print()

'''
# ASCII American standard code for information interchange
# 7 bit code  1000001 1010101 0100101
#               34       76      78

input = 65

for i in range(1, 6):
    for j in range(1, i + 1):
        print(chr(input), end = ' ' )
        input = input + 1
    print()














list1 = ["gigg", "b", "c", "d"]
list2 =[("gigg", "x"), ("b", "y"), ("e", "z"), ("d", "a")]
matchlist = []
unmatched = []

for i in list1:
    for a, b in list2:  # <-- this unpacks the tuple like a, b = (0, 1)
        if i == a:
            matchlist.append(b)
            print("match list:",matchlist)
        else:
            unmatched.append(b)
            print("unmatched list:", unmatched)


str = 'mani'
str1 = str.replace('m', 'n')
print(str1)

'''