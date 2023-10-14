# File: <Dice Rolling Function>
# Description: <In a program, write a function named roll that accepts an integer argument number_
# of_throws. The function should generate and return a sorted list of number_of_throws
# random numbers between 1 and 6. The program should prompt the user to enter a positive
# integer that is sent to the function, and then print the returned list.>
# Assignment Name and Number: Dice Rolling Function , #7.6
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

def main():
    print()
    print('This program will roll a die as many times as you like.')
    try:
        num_of_throws = int(input("Please enter a positive ineteger to decide the number of throws: "))
        if num_of_throws < 1:
            print('Error!, you did not enter a positive integer.')
        else:
            final = roll(num_of_throws)
            print('The list of random numbers are: ', final)
    except ValueError:
        print('Error!!, please enter a positive integer.')
    print()
   



def roll(num_of_throws):
    if num_of_throws < 1:
        return []
    numbers = []
    for x in range(num_of_throws):
        rand_num = random.randint(1, 6)
        numbers.append(rand_num)

    return numbers

main()