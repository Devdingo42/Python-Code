# File: <Population>
# Description: <Write a program that predicts the approximate size of a population of organisms. The
#application should use text boxes to allow the user to enter the starting number of organisms, the average daily population increase (as a percentage), and the number of days the
#organisms will be left to multiply.>
# Assignment Name and Number:Population, #4.13
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

print()
print('This program will approximate the size of a population of organisms')
Starting_number = int(input('Please enter the starting number of organisms: '))
Increase = int(input('Please enter the average daily population increase (as a percentage): '))
Days = int(input('Please enter the number of days the organisms will be left to multiply: '))

print()
print('Day Approximate\tPopulation')
print('---------------------------')

for Days in range(1, Days + 1):
    total = Starting_number
    Starting_number *= (1+(Increase/100))
    print(Days, ' \t\t', format(total, ',.2f'))