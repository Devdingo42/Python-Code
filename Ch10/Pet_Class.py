# File: <Pet_Class>
# Description: <Once you have written the class, write a program that creates an object of the class and
#prompts the user to enter the name, type, and age of his or her pet. This data should be
#stored as the object’s attributes. Use the object’s accessor methods to retrieve the pet’s
#name, type, and age and display this data on the screen.>
# Assignment Name and Number: Pet Class, #10.1
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    
    def set_age(self, age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
        
def main():
    again = 'y'

    while again == 'y':
        print()
        nm = input('Enter the name of the pet: ')
        animal= input('Enter the type of animal the pet is: ')
        a = input('Enter the age of the pet: ')
        pe = Pet(nm, animal, a)
        print()
        print('Here is the data you have entered about your pet.')
        print('Name: ', pe.get_name())
        print('Animal Type: ', pe.get_animal_type())
        print('Age: ', pe.get_age())
        another = input('Do you have another pet? ' + '(Enter y for yes): ')

main()