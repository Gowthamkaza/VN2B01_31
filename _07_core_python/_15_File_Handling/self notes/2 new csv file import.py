import csv

f2=open("E:\Gowtham vn2 files\VN2B01_031-master\_07_core_python\_15_File_Handling\Class notes\student1.csv",'r')
print(f2.read())
f2.close()

#trying to import jpeg image
f3=open('E:\Gowtham vn2 files\VN2B01_031-master\_07_core_python\Acii codes.jpeg','rb')  #read binary
f4=open("my pic",'wb')
for i in f3:
    f4.write(i)