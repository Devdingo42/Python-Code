#Hot Dog Cookout Calculator
#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a
#program that calculates the number of packages of hot dogs and the number of packages of
#hot dog buns needed for a cookout, with the minimum amount of leftovers. The program
#should ask the user for the number of people attending the cookout and the number of hot
#dogs each person will be given. The program should display the following details:
#The minimum number of packages of hot dogs required
#The minimum number of packages of hot dog buns required
#The number of hot dogs that will be left over
#The number of hot dog buns that will be left over

#Set Values
hotdogs = 10
buns =8

#User input
print()
attendance = int(input('Please enter the number of people attending the cookout: '))
print()
number_hot_dogs_given = int(input('Please enter the number of hot dogs each person will be given: '))

number_of_hotdogs =  number_hot_dogs_given * attendance

print()

if number_of_hotdogs > 0:
    print('The minimum amount of hot dog packages required is', round((number_of_hotdogs + 4) / hotdogs), 'packages')
if number_of_hotdogs > 0:
    print('The minimum amount of hot dog bun packages required is', round(number_of_hotdogs + 4) // buns, 'packages')

print('The amount of leftover hotdogs are', number_of_hotdogs % hotdogs, 'hotdogs')

print('The amount of leftover buns are', number_of_hotdogs % buns, 'buns')