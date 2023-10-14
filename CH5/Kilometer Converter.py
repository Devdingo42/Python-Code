# File: <Kilometer Converter>
# Description: <Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles>
# Assignment Name and Number: Kilometer Converter, #5.1
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

#Get user input
def main():
    print()
    print('This program will convert kilometers to miles.')
    global kilometers
    kilometers = int(input('Please enter a distance in kilometers: '))
    result = miles()
    print('The conversion of', kilometers,'km to miles is', result,'miles.')
    print()

def miles():
    miles = kilometers * 0.6214
    return miles

main()