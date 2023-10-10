# File: <Largest List Item>
# Description: <Design a function that accepts a list as an argument and returns the largest value in the list.
# The function should use recursion to find the largest item.>
# Assignment Name and Number: Largest List Item, #12.4
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

num1 = int(input("Please enter a random positive whole number: "))
num2 = int(input("Please enter a random positive whole number: "))
num3= int(input("Please enter a random positive whole number: "))
num4 = int(input("Please enter a random positive whole number: "))
num5= int(input("Please enter a random positive whole number: "))



def main():
    List = [num1, num2, num3, num4, num5]
    print('The largest number in the list is', range_large(List))

def range_large(num_list):
    if len(num_list) == 1:
        return num_list[0]
    n = range_large(num_list[1:])
    if num_list[0] > n:
        return num_list[0]
    else:
        return n  
main()