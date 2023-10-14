# File: <Falling Distance>
# Description: <Write a function named falling_distance that accepts an object’s falling time (in seconds)
# as an argument. The function should return the distance, in meters, that the object has
# fallen during that time interval. Write a program that calls the function in a loop that passes
# the values 1 through 10 as arguments and displays the return value.>
# Assignment Name and Number: Falling Distance, #5.13
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.



def main():
   for fallingtime in range(1, 11):
      times = falling_distance(fallingtime)
      print('The distance is', format(times, '.2f'), 'meters at', fallingtime, 'seconds.')

def falling_distance(time):
   gravity = 9.8
   distance = (.5) * (gravity) * (time ** 2)
   return distance


main()