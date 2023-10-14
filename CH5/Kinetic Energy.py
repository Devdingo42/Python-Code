# File: <Kinetic Energy>
# Description: <Write a function named kinetic_energy that accepts an object’s mass (in kilograms)
#and velocity (in meters per second) as arguments. The function should return the amount
#of kinetic energy that the object has. Write a program that asks the user to enter values
#for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic energy.>
# Assignment Name and Number: Kinetic Energy, #5.14
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    print()
    print('This program will calculate Kinetic Energy.')
    mass = int(input('Pleae enter a value for mass: '))
    velocity = int(input('Please enter a value for velociy: '))
    KE = kinetic_energy(mass, velocity)
    print("The objects kinetic energy is", format(KE, '.2f'), 'mass/velocity^2 or KE.')

def kinetic_energy(a, b):
    Kinetic_energy = (1/2) * (a) * (b ** 2)
    return Kinetic_energy

main()