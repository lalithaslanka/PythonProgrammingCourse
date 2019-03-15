'''
Write a program that writes 100 integers created randomly into a file.
Integers are separated by a space in the file. Read the data back from the file and
display the sorted data. Your program should prompt the user to enter a filename. If the
file already exists, do not override it.
'''

import os
import random

fname = input("Enter the new file name")
file_exists = True
while file_exists:
    if os.path.exists(fname):
        file_exists = True
        print("File already exists")
        fname = input("Enter the new file name")
    else:
        file_exists = False

f = open(fname,'w+')
for i in range(1,100):
    f.write(str(random.randint(1,101))+" ")
f.close()
print("File Created")

f = open(fname,'r')
numbers = []

for line in f:
    numbers_in_line = line.split(" ")
    numbers = [int(i) for i in numbers_in_line]

print(numbers.sort())

f.close()

        
