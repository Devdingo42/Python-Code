# File: <Rock, Paper, Scissors Game>
# Description: <Write a program that lets the user play the game of Rock, Paper, Scissors against the computer>
# Assignment Name and Number: Rock, Paper, Scissors Game, #5.21
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import random

def main():
    print()
    print('This program will play rock, paper, scissors against you')
    user_answer = (input('Please enter rock, paper, or scissors: '))
    comp_answer = comp()
    if comp_answer == 'rock' and user_answer == 'scissors':
        print('The computer won!!!')
    elif comp_answer == 'scissors' and user_answer == 'rock':
        print('You won!!!!')
    elif comp_answer == 'paper' and user_answer == 'rock':
        print('The computer won!!!')
    elif comp_answer == 'rock' and user_answer == 'paper':
        print('You won!!!!')
    elif comp_answer == 'paper' and user_answer == 'scissors':
        print('You won !!!!')
    elif comp_answer == 'scissors' and user_answer == 'paper':
        print('The computer won!!!')
    elif comp_answer == 'paper' and user_answer == 'paper':
        print("You tied.")
        return main()
    elif comp_answer == 'rock' and user_answer == 'rock':
        print('You tied.')
        return main()
    elif comp_answer == 'scissors' and user_answer == 'scissors':
        print('You tied')
        return main()



def comp():
    for count in range(1):
        answer = random.randint(1, 3)
        if answer == 1:
            print('The computer chose rock.')
            result = 'rock'
        elif answer == 2:
            print('The computer chose paper.')
            result = 'paper'
        elif answer == 3:
            print('The computer chose scissors.')
            result = 'scissors'
        return result


main()