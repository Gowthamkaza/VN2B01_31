print("----------write operation-------")
file=open("read and write operation.txt",'w')
file.write("the data of python is implemented")
file.write('\n  as new programing language')
file.write('\n it is high level languge')
file.close()


print("----------r+ operation-------")
#Read and Write (‘r+’)
#pointer is placed before the content
file=open("read and write operation.txt",'r+')
print(file.read())
file.write("\n the new things are added")
file.close()


print("----------w+ operation-------")
#Write and Read ('w')
#pointer is placed after the content
file=open("read and write operation.txt",'w+')
file.write("python is used in multiple companies")
file.seek(0)
print(file.read())
file.close()


print("---------a+ operation--------")
file=open("read and write operation.txt",'a+')
file.write('\n python having frame works')
file.seek(0)
print(file.read())
file.close()


print("inserting image")
f=open('Acii codes.jpeg','rb')
f1=open("my pic.jpg",'wb' )
for i in f:
    f1.write(i)

f.close()























