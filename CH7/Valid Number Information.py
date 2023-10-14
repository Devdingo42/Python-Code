# File: <Valid Number Information>
# Description: <Design a program that uses a loop to build a list named valid_numbers that contains only
# the numbers between 0 and 100 from the numbers list below. The program should then
# determine and display the total and average of the values in the valid_numbers list.>
# Assignment Name and Number: Valid Number Information, #7.1
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
  print()
  numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
  index = 0
  valid_numbers = []

  for number in numbers:
     if 0 <= number <= 100:
        valid_numbers.append(number) 
        index += number 

  average = index / len(valid_numbers)
  
  print("The valid numbers are:", valid_numbers)
  print("The total of the numbers is:", index)
  print("The average of the numbers is:", format(average, '.2f'))
  print()

main()