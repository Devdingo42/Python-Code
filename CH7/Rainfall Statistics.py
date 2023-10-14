# File: <Rainfall Statistics>
# Description: <Design a program that lets the user enter the total rainfall for each of 12 months into a
# list. The program should calculate and display the total rainfall for the year, the average
# monthly rainfall, the months with the highest and lowest amounts.>
# Assignment Name and Number: Rainfall Statistics, #7.3
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

Num_months = 12

def main():
    print()
    rainfall = [0] * Num_months
    index = 0
    while index < Num_months:
        print('Enter the amount of rainfall for Month #', index + 1, ': ', sep='', end='')
        rainfall[index] = float(input())
        index += 1
    total = 0
    for value in rainfall:
        total += value
    print('The total amount of rainfall over the 12 months is: ', total)
    average = total/ len(rainfall)
    print('The average amount of rainfall during the 12 months is: ', average)
    rainfall.sort()
    print('The month with the lowest amount of rainfall produced only: ', rainfall[0],)
    print('The month with the highest amount of rainfall produced as much as: ', rainfall[11])
    print()
    
main()