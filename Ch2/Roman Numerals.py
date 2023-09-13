#Roman Numerals
#Write a program that prompts the user to enter a number within the range of 1 through 10.
#The program should display the Roman numeral version of that number. If the number is
#outside the range of 1 through 10, the program should display an error message.

#User Input
print()
print("This program will convert your whole number into a Roman Numeral")
number = int(input("Please enter a whole number within the range of 1-10: "))

#Roman Numeral Conversion
if number == 1:
    print("The roman numeral of the number 1, is I")
elif number == 2:
    print("The roman numeral of the number 2, is II")
elif number == 3:
    print('The roman numeral of the number 3, is III')
elif number == 4:
    print('The roman numeral of the number 4, is IV')
elif number == 5:
    print('The roman numeral of the number 5, is V')
elif number == 6:
    print('The roman numeral of the number 6, is VI')
elif number == 7:
    print('The roman numeral of the number 7, is VII')
elif number == 8:
    print('The roman numeral of the number 8, is VIII')
elif number == 9:
    print('The roman numeral of the number 9, is IX')
elif number == 10:
    print('The roman numeral of the number 10, is X')
else:
    print("Error!!!, You did not correctly enter within the range, Error!")