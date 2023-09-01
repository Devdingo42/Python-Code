#Circle Measurements
#Write a program that asks the user to enter the radius of a circle. 
#The program should calculate and display the area and circumference of the circle using πr for the area
#2πr for the circumference.

#Asking for user input
radius = float(input('What is the radius of the Circle?'))

#Area and Circumference

area = float(3.14159 * radius**2)
circumference = float(2 * 3.14159 * radius)

#Display to user
print("The area of the circle is", area, "feet")
print('The circumference of the circle is', circumference, 'feet')