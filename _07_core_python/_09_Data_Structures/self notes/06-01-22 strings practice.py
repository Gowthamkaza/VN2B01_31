x="hello world"
print(x.capitalize())   #capitalize

x="THE BASI REDDY"
print(x.casefold())       #Case

Y="THE ALGARITHUM OF PYTHON"
print(Y.center(80))         #center

z="basi reddy got new laptop"
print(z.count("d"))        #count

v="the nature is beautiful"
t=v.encode()                #encode
print(t)

z=t.decode()                    #decode
print(z)

h="vey good."
x=h.endswith(".")               #ends with".", Returns true if the string ends with the specified value
print(x)

h="very bad$"
x=h.endswith("$")                #ends with"$", Returns true if the string ends with the specified value
print(x)

txt="hello"
txt="H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))            #Sets the tab size of the string
print(txt.expandtabs(6))
print(txt.expandtabs(10))

string=("the weather is cold today")
x=(string.find("i"))                        #Text find
print(x)
y=(string.find("e",8,10))                       #text find in between range
print(y)

#named indexes by format:
txt1 = "My name is {change}, I'm {details}".format(change = "John", details = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",26)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",26)

print(txt1)
print(txt2)
print(txt3)

tx3="my name is {tell}, my {details} is 26".format(tell="gowtham",details="age")    #named index
print(tx3)
tx4="my name is {},i'm {}".format("gowtham",26)
print(tx4)



txt = "Company 12"
x = txt.isalnum()           #is alpha numeric ,!=  alphabet letter (a-z) and numbers (0-9). return false
print(x)

txt = "Company12"
x = txt.isalnum()           #alphabet letter (a-z) and numbers (0-9). if satisfies returns  true
print(x)

p1= "CompanyX"
x = p1.isalpha()            #is aplha if satisfies true
print(x)

p1= "CompanyX1"
x = p1.isalpha()            #is aplha if not satisfies true
print(x)



a="Hello This is gowtham" #@1!"
b=a.isprintable()       #Check if all the characters in the text are printable:
print(b)

print("------------up to characters printable is completed ------------")

a=" "
b=a.isspace()           #Check if all the characters in the text are whitespaces:
print(b)

a="Hi Everyone This Is gowtham"
b=a.istitle()           #Returns True if the string follows the rules of a title
print(b)

c="the thing is terminal"  #title string
d=c.istitle()           #returns false if the string is does not satisfies the condition
print(d)
a="Hello every one"      #upper string
b=a.isupper()           #Returns True if all characters in the string are upper case or else returns false
print(b)

a="HELLO THIS IS GOWTHAM"
b=a.isupper()           #Returns True if all characters in the string are upper case or else returns false
print(b)

a=("pen",'paper','notes')
b= " and ".join(a)          #Join all items in a tuple into a string, using and character as separator:
print(b)

a=("pen",'paper')   #Join all items in a tuple into a string, using a hash character as separator:
b="#".join(a)
print(b)

h1 = "python world"
x =h1.ljust(20)              #Return a 10 characters long, left justified version of the word "Uday":
print(x, "has more future.")


p = "HELLO my FRIENDS"          #Converts a string into lower case
k =p.lower()
print(k)

txt = "     Gowtham     "
t7 = txt.lstrip()                   #Remove spaces to the left of the string
print("This is", t7, "kaza")

txt45 = "Hello ram!"
j78 = txt45.maketrans("r", "s")     #changes of translate()
print(txt45.translate(j78))         #Returns a translation table to be used in translations

txt = "I could eat bananas all day"   #Returns a tuple where the string is parted into three parts
x = txt.partition("bananas")
print(x)


s7= "I like bananas"                         #replace
s8= s7.replace("bananas", "apples")
print(s8)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")             #replace with repetation range of words
print(x)

#The rfind() method is almost the same as the rindex()
txt = "Hello, this is python entrance."      #Searches the string for a specified value
x = txt.rfind("e")                          #and returns the last position of where it was found
print(x)

txt = "this is raghav, he is went out."
h10= txt.rindex("is")
print(h10)

s15= "ice cream"        #Returns a right justified version of the string
s16 = s15.rjust(20)     #rjust
print(s16, "is my favorite.")

#Splits the string at the specified separator, and returns a list
# rsplit :   Split a string into a list, using comma, followed by a space (, ) as the separator

y5= "telugu, english, science"
y7 = y5.rsplit(", ")
print(y7)

y5= "telugu, english, science" # setting the maxsplit parameter to 1, will return a list with 2 elements!
y7 = y5.rsplit(", ", 1)
print(y7)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()            #Splits the string at the specified separator, and returns a list
print(x)

#startswith() ---Returns true if the string starts with the specified value
s67 = "Hello, welcome to my world."
s68 = s67.startswith("Hello")
print(s68)

#strip()-----	Returns a trimmed version of the string
#Remove spaces at the beginning and at the end of the string:

h23= "     raghavendra     "
h24= h23.strip()
print("he is", h24, "from nellore")

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
name = "Hello My Name Is Gowtham"
g5= name.swapcase()
print(g5)

# title()	Converts the first character of each word to upper case
texty= "Welcome to python world"
result= texty.title()
print(result)














