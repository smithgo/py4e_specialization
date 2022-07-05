# 2022.07.05
# Exercise 7.1
# Write a program to read through a file and print the contents of the file (line by line) all in upper case.
fhand = open('mbox-short.txt')
for line in fhand :
    linestripped = line.rstrip()
    print(linestripped.upper())