#Write a program that removes all the occurrences of a specified string from a text file.
#Your program should prompt the user to enter a filename and a string to be removed.

import os

file_name = input("Enter the file name")
file_not_found = True
while file_not_found:
    if os.path.exists(file_name):
        file_not_found = False
        print("File found")
    else:
        file_not_found = True
        print("File not found")
        file_name = input("Enter a valid file name")

file_handler = open(file_name,'r')
print("File openined")
if not file_handler.read():
    print("No content in file")
else:
    new_file_list=[]
    for line in file_handler:
        print(line)
        line.replace("morning","")
        print(line)
        new_file_list.append(line)
file_handler.close()

file_handler.writeline(new_file_list)
file_handler.close()
    
    
    
        
    
    

        

