# File: <Recursive Multiplication>
# Description: <Design a recursive function that accepts two arguments into the parameters x and y. The function should return the value of x times y.>
# Assignment Name and Number: Recursive Multiplication, #12.2
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

number_1 = int(input('Please enter a nonnegative itenger: '))
number_2 = int(input('Please enter a nonnegative itenger: '))

def value(a, x):
    if x == 0 and a == 0:
        return 0
    elif a == 1:
        return x
    else:
        return value(a-1, x) + x

result = value(number_1, number_2)

print('The value of', number_1, 'and', number_2, "is", result)
