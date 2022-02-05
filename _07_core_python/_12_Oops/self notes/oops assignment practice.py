#  Find length of given string   ie., "Gowtham kaza"
# by built in function approach
x=input("enter the string:")
print(len(x))

#algorithumapproach

print("using algorithum approach",)
str1=input("enter the string:")
count=0
for i in str1:
    count+=1
    print('length of the string',count)

    #using function

print("-------3. With functions-------")

str1 = input("Enter the string:")

def find_length(in_str=None):
    le = 0
    for char in in_str:
        le += 1
    return le
print("Length of string : ", find_length(str1))


#Count characters in string
print("------- Count characters in string-------")
# by built in function approach
x=input("enter the string:")
print(count(x))