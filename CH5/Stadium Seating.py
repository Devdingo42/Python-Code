# File: <Stadium Seating>
# Description: <There are three seating categories at a stadium. Class A seats cost $20, Class B seats cost $15, and Class C seats cost $10. Write a
# program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.>
# Assignment Name and Number: Stadium Seating, #5.7
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    print()
    print('This program will display the amount of income generated from ticket sales.')
    print('Class A = $20.')
    print('Class B = $15.')
    print('Class C = $10.')
    A = classA()
    B = classB()
    C= classC()
    Income = A + B + C
    print('The amount of income generated from ticket sales is $', Income,)

def classA():
    Money_A = int(input('How many tickets for class A seats were sold: '))
    Total_A = Money_A * 20
    return Total_A

def classB():
    Money_B = int(input('How many tickets for class B seats were sold: '))
    Total_B = Money_B * 15
    return Total_B

def classC():
    Money_C = int(input('How many tickets for class C seats were sold: '))
    Total_C = Money_C * 10
    return Total_C

main()