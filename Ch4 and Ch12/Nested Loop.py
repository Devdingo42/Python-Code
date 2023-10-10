# File: <Nested Loop>
# Description: <Write a program that uses nested loops to draw this pattern.>
# Assignment Name and Number: "Write a program that uses nested loops to draw this pattern", #4.14
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.


Top_SIZE = 7

for r in range(Top_SIZE):
    for c in range(7-r):
        print('* ', end='')
    print()