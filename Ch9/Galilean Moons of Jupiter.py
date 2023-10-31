# File: <Galilean Moons of Jupiter>
# Description: <The program should let the user enter the name of a Galilean moon of Jupiter, then it
# should display the moon’s mean radius, surface gravity and orbital period.>
# Assignment Name and Number: Galilean Moons of Jupiter, #9.1
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

Moon1 = 'Io'
Moon2 = 'Europa'
Moon3 = 'Ganymede'
Moon4 = 'Callisto'

def main():
    print()
    radius = {'Io':'1821.6 km', 'Europa':'1560.8km', 'Ganymede':'2634.1km', 'Callisto':'2410.3km' }
    surface_gravity = {'Io':'1.796', 'Europa':'1.314', 'Ganymede':'1.428', 'Callisto':'1.235' }
    orbital_periods = {'Io':'1.796 days', 'Europa':'3.551 days', 'Ganymede':'7.154 days', 'Callisto':'16.689 days' }
    print('This program will give you a Galilean moon of your choice, and display the radius, surface gravity and orbital period.')

    print()
    
    choice = user_choice()

    print()

    if choice in radius:
        print('The radius around the moon', choice, "is", radius[choice])
    if choice in surface_gravity:
        print('The surface gravity on the moon', choice, 'is', surface_gravity[choice])
    if choice in orbital_periods:
        print('The orbital periods on the moon', choice, 'is', orbital_periods[choice])
    print()

def user_choice():
    print('THE GALILEAN MOONS OF JUPITER')
    print('-----------------------------')
    print('Io')
    print('Europa')
    print('Ganymede')
    print('Callisto')
    choice = input('Please enter the moon you would like to see: ')
    while choice != Moon1 and choice != Moon2 and choice != Moon3 and choice != Moon4:
        choice = input('Please enter one of these moons: ')
    return choice


   

main()