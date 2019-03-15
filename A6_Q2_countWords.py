#(Count characters, words, and lines in a file) Write a program that will count
#the number of characters, words, and lines in a file. Words are separated by a whitespace character.
#Your program should prompt the user to enter a filename.

import os

fname = input("Enter the file name")
file_not_found = True
while file_not_found:
    if os.path.exists(fname):
        file_not_found = False
        print("File found")
    else:
        file_not_found = True
        print("File not found")
        fname = input("Enter a valid file name")
infile = open(fname, 'r')
lines = 0
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    lines = lines + 1
    words = words + len(wordslist)
    characters = characters + len(line)
print(lines, " Lines")
print(words, " Words")
print(characters, " characrters")
