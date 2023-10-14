# File: <Lottery Number Generator>
# Description: <Design a program that generates a seven-digit lottery number. The program should generate seven random numbers, each in the range of 0 through 9, and assign each number to a
# list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
# displays the contents of the list.>
# Assignment Name and Number: Lottery Number Generator, #7.2
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

#Lottery Number
def main():
    print()
    lot_number = []
    for x in range(7):
        number = random.randint(0,9)
        lot_number.append(number)
    print('The lottery number is,')

    for n in lot_number:
        print (n, end='')
    print()

main()