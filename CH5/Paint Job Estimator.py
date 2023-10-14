# File: <Paint Job Estimator>
# Description: <A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of labor will be required. 
# The company charges $35.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the
# paint per gallon.>
# Assignment Name and Number: Paint Job Estimator, #5.8
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import math



def main():
    print()
    square_feet = int(input('Enter the square feet of wall space to be painted: '))

    price_paint = int(input('Enter the price of the paint per gallon: '))

    final(square_feet, price_paint)

def final(square_feet, price_paint):
    number_of_gallons = math.ceil(square_feet / 112)
    labor = number_of_gallons * 8
    cost_of_labor = labor * 35
    total_paint = number_of_gallons * price_paint
    result = cost_of_labor + total_paint
    print('The number of gallons of paint required is', number_of_gallons, 'gallons.')
    print('The hours of labor required is', labor, 'hours')
    print('The cost of the paint is', total_paint, sep=' $')
    print('The labor charges is', cost_of_labor, sep=' $')
    print('The total cost of the paint job is', result, sep=' $')

main()