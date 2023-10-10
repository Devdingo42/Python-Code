# File: <Calculating the Factorial of a Number>
# Description: <Write a program that lets the user enter a nonnegative integer then uses a loop to calculate
#the factorial of that number. Display the factorial.>
# Assignment Name and Number: Calculating the Factorial of a Number, #4.12
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

print()
print('This program will calculate the factorial of the number you chose.')
number = int(input('Please enter a nonnegative integer: '))

total = 1
print()
if number >= 1:
    for num in range(1, number +1):
        total *= num
else:
    print("Error!, you did not enter a nonnegative number or 0 ")
if total > 1:
    print("The Factorial of", number, "is", total)
print()