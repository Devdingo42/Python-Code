#Roulette Wheel Colors
#Write a program that asks the user to enter a pocket number and displays whether the
#pocket is green, red, or black. The program should display an error message if the user
#enters a number that is outside the range of 0 through 36.

#User Input
print()

number = int(input('Please enter a whole number from the range 0 through 36: '))

print()
if number >= 0 and number <= 36:
    if number == 0:
        print('You chose 0, the pocket number is green.')
    elif number == 1 or number == 3 or number == 5 or number == 7 or number == 9:
        print('The pocket number is red.')
    elif number == 2 or number == 4 or number == 6 or number == 8 or number == 10:
        print('The pocket number is black.')
    elif number == 11 or number == 13 or number == 15 or number == 17:
        print('The pocket number is black.')
    elif number == 12 or number == 14 or number == 16 or number == 18:
     print('The pocket number is red.')
    elif number == 19 or number == 21 or number == 23 or number == 25 or number == 27:
     print('The pocket number is red.')
    elif number == 20 or number == 22 or number == 24 or number == 26 or number == 28:
     print('The pocket number is black.')
    elif number == 29 or number == 31 or number == 33 or number == 35:
        print('The pocket number is black')
    elif number == 30 or number == 32 or number == 34 or number == 36:
        print('The pocket number is red.')
else:
    print("Erorr!, You did not enter a correct value in the range ")
print()