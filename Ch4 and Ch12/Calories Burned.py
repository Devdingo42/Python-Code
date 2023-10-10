# File: <Calories Burned>
# Description: <Running on a particular treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes>
# Assignment Name and Number: Calories Burned #4.2
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

Calories_per_minute = 4.2

print('I will display the Calories burned after 10, 15, 20, 25, and 30 minutes')
for num in [10, 15, 20, 25, 30]:
    print('At', num, 'minutes, you will burn', num * Calories_per_minute, 'calories')
