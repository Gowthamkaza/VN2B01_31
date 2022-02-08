print('"x" - Create - Creates the specified file, returns an error if the file exists')
#f=open("create anew file.txt","x")
f=open("create anew file.txt",'w')
f.write("this is the first \n ")
f.write("last file practicising")
f.close()

f=open("create anew file.txt",'r')
print(f.read())
f.close()

f=open("create anew file.txt",'a')
f.write("\n adding another assignment")
f.close()




print("creating new .py file by file handling")
f=open("new file.py",'w')
f.close()

print("creating pdf files")
f=open("new file.pdf",'w')



f=open("file3.txt",'w')
f.write("the 3rd program writing is ")
f.write("\n adding w+ operation")
f.close()


#split() using file handling
print("------slicing")
with open("read and write operation.txt",'r') as file3:
    data3=file3.readlines()
    for line in data3:
        word=line.split()
        print(word)