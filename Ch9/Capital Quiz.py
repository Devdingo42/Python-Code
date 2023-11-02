# File: <Capital Quiz>
# Description: <Write a program that creates a dictionary containing the U.S. states as keys, and their capitals as values. 
#The program should then randomly quiz the user by displaying the name of a state and asking the user
#to enter that state’s capital. The program should keep a count of the number of correct and incorrect responses.>
# Assignment Name and Number: Capital Quiz, #9.2
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


def main():
    print()
    print('This program will quiz you on your knowledge on the US States and their Capitals.')
    States = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 
              'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover',
                'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 
                'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka', 
                'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 
                'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson', 
                'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 
                'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 
                'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 
                'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 
                'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 
                'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}
    
    length = len(States)
    state_list = list(States)

    correct = 0
    incorrect = 0

    for count in range(length):
        print()
        state = (random.choice(state_list))
       # state, capital = random.choice(state)
        print((state))
        ans = input('Enter the capital of this state: ')
        print()
        if (ans == States[state]):
            correct += 1
            print('Correct')
            state = state_list.remove(state)

        else:
            incorrect += 1

            print('Incorrect, the answer of', state, 'is', States[state])
            state = state_list.remove(state)


    print('You have',correct,'correct answers')
    print('You have',incorrect,'incorrect answers')

main()