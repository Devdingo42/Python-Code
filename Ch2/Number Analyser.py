#Number Analyser
#Write a program that asks the user to enter an integer.
# The program should display “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and 
#“Zero” if the number is equal to 0. The program should then display “Even” if the number
#is even, and “Odd” if the number is odd.

#User input
integer = int(input ('Enter an integer: '))
print()
#Negative positivve
if integer < 0:
    print('The number you inserted is Negative.')
elif integer > 0:
    print('The number you inserted is Positive.')
elif integer == 0:
    print ('The number you inserted is Zero.')
#Even or Odd
if integer % 2 == 0:
    print('The number is even.')
else: 
    print("The number is odd.")