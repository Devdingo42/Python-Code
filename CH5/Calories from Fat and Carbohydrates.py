# File: <Calories from Fat and Carbohydrates>
# Description: <A nutritionist who works for a fitness club helps members by evaluating their diets. As part
# of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day>
# Assignment Name and Number: Calories from Fat and Carbohydrates, #5.6
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

def main():
    print()
    print('This program will calculates the number of calories that result from the fat and carbs of the food you ate.')
    calories_fat()
    calories_carbs()

def calories_fat():
    fat = int(input('Please enter the number of fat grams you have had today: '))
    calories_fat = fat * 9
    print("The amount of calories that came from the number of fat grams are", calories_fat, 'calories.')

def calories_carbs():
    carbs = int(input('Please enter the number of carb grams you have had today: '))
    calories_carbs = carbs * 4
    print("The amount of calories that came from the number of carb grams are", calories_carbs, 'calories.')

main()