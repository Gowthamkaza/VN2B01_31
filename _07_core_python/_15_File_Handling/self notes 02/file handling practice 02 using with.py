#open file using with statement
with open('new file.txt','w') as txt_case1:
    txt_case1.write('this is gowtham')


# working with Binary Files
# #two operations are occured in this rb,wb.
#rb- read binary, wb- write binary

#creating binary in output
file1=open("images.jpg","rb")
for i in file1:
    print(i)
#importing  image one path to another path
file2=open("images.jpg",'rb')
file3=open("created image.jpg",'wb')
f=file2.read()
file3.write(f)
file2.close()
file3.close()

print("----pickling and unpickling------")
'''
The process to converts any kind of python objects (list, dict, etc.) into byte streams 
(0s and 1s) is called pickling or serialization or flattening or marshalling. 

We can converts the byte stream (generated through pickling) back into python objects by a 
process called as unpickling
for pickling: syntax: pickle.dump(object, file)
for unpickling: syntax: object=pickle.load(file)
'''
import pickle
def write():
    list = ['ravi', 'ramesh', '1', '5']
    f=open("binary file1.txt",'wb')
    pickle.dump(list,f)
    f.close()

write()

def read():
    f=open("binary file1.txt",'rb')
    list2=pickle.load(f)
    print(list2)
    f.close()
read()


print("--------seek and tell method------")
'''seek():
-------
To move file pointer from one point to another, use seek() method.it makes two arguments

f.seek(offset, fromwhere)'''
file5=open('state1.txt','r+')
file5.write("To move file pointer from one point to another, use seek() method.\n it makes two arguments")
file5.seek(0)
print("pointer starts with zero")
#print(file5.seek(0))
file5.seek(10,0)
#print(file5.read())
#print(file5.readline())
print(file5.readlines())
file5.write("\n offset - represents how many bytes to move")
print(file5.read())
print("tell denotes pointer location",file5.tell())




