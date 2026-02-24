# Name : Gabriel Egan Gakere
# Date : 24/02/2026
# A program to show file input and output in python

# Creating a new file
new_file = open("student_data.txt","r+")





# Writting to a file
new_file.write("{ Student name : Gabriel Egan Gakere, ID : 290839, Email : gabriel.egan.gakere@inspire.org.uk }")




# Reading from a file
new_file = open("student_data.txt","r+")

data = new_file.read()
print(data) 
new_file.close()


#delete file
import os
os.remove("student_data.txt")


# Deliting a folder
os.rmdir("my_folder")