# File: <Pennies for Pay>
# Description: <Write a program that calculates the amount of money a person would earn over a period of
#time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display
#a table showing what the salary was for each day, then show the total pay at the end of the
#period. The output should be displayed in a dollar amount, not the number of pennies.>
# Assignment Name and Number: Pennies for Pay, #4.7
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

total= 0.0
Penny = 0.01


print('This program will double the amount of a penny every day, for as many days that you input')
Days = int(input('Input the amount of days that you want the penny to double: '))
print()
print('Days\tSalary')
print('--------------')
if Days < 0:
     print('Error, Enter a whole number above 0')
for Days in range (1, Days +1):
    salary = Penny
    Penny *= 2
    print(Days, '\t',"$", salary) 
print()
total= salary
print('Your total salary is $', total)
print()