print("-----creating a file storage----")
file=open("file.txt",'w')
file.write("new file is created \n")
file.write("this is gowtham")
file.close()

print("-----override the previous data----")
file=open("file.txt",'w')
file.write("Gowtham  \n")
file.write("welcome to vn2 solutions ")
file.close()


