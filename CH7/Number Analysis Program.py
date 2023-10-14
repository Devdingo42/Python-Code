# File: <Number Analysis Program>
# Description: <Design a program that asks the user to enter a series of 20 numbers. The program should
# store the numbers in a list then display the following data:
# •	 The lowest number in the list
# •	 The highest number in the list
# •	 The total of the numbers in the list
# •	 The average of the numbers in the list>
# Assignment Name and Number: Number Analysis Program, #7.4
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

Num_numbers = 20

def main():
    print()
    numbers = [0] * Num_numbers
    index = 0
    while index < Num_numbers:
        print('Enter any number for Number #', index + 1, ': ', sep='', end='')
        numbers[index] = float(input())
        index += 1
    print()
    numbers.sort()
    print('The lowest number in the list is: ', numbers[0],)
    print('The highest number in the list is: ', numbers[19])
    total = 0
    for value in numbers:
        total += value
    print('The total of all the numbers is: ', total)
    average = total/ len(numbers)
    print('The average of all the numbers is: ', average)
    print()
    
main()