#*-*-*-*-*-*-*-*-*-*-*-*-*File_Handling*-*-*-*-*-*-*-*-*-*-*-*--
# First We Created a file name as Myfile.txt then we use here readlines mode to read the Content of Myfile.txt  line by line
a = open("Myfile.txt","r") # Created file and make it at read mode to read the content of file 
c = a.readlines()  #readline will read the first row written in the txt file if we again call readline it will read the next line
print(c)
a.close()   # this will close the file that we have opened it is very important to close the file

# We Use Here Read(r) Mode it will read entire file
# file=open("myfile.txt","r")
# print(file.read())
# file.close()

# We use here write Mode
# file= open("Myfile.txt","w") # this will open the file in the write mode
# file= file.write("Hii Have a nice Day\nWhat is the plan tomorrow\n yes going to play cricket\n thanks")  # it will write the data in the created txt file
# print(file)
# #file.close()

# try and except part of file handling this is use to check whether the file exist or not
try:
    file = open("Myfile.txt","r") # this will check that file is exist or not if file name is not exist then it will throw an error message
    print(file.read())
    file.close()
except :                       #this is an exception it will print the error message
    print("file did not exist")

#*************-----**************---------**************---------**********-------******
#Now We Wil Create a New file by using (x) keyword this will create a new file with x keyword
# file = open("hello.txt","x")  # it will create a new file
# file.close()

# #New File to read(r) this created file we have write this code
# file = open("hello.txt","r")
# content = file.read()
# print(content)
# file.close()

#New file Append(a) function we use and added some data in file
# file = open("hello.txt","a")     #append function will add data which we written and many time we run it will print that data again and again
# d = file.write("\nTata Motors is a good")
# print(d)
# file.close()

# Deleting a File
# import os
# os.remove("hello.txt")  # Deletes the file
# if os.path.exists("hello.txt.txt"):   #Check if the file exists before deleting to avoid errors:
#     os.remove("hello.txt")
# else:
#     print("The file does not exist")

