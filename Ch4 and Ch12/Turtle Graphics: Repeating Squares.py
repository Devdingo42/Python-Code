# File: <Turtle Graphics/ Repeating Squares>
# Description: <In this chapter, you saw an example of a loop that draws a square. 
# Write a turtle graphics program that uses nested loops to draw 100 squares, to create the design shown in Figure 4-13>
# Assignment Name and Number: "Turtle Graphics: Repeating Squares", #4.16
#
# Name: <Devon Duplessie>
# GitHub: <Devdingo42>
#
# On my honor, <Devon Duplessie>, this programming assignment is my own work
# and I have not provided this code to any other student.

import turtle

Num_Squares = 100
OFFSET = 5
Animation_speed = 0
length = 10
turn = 90
turtle.speed(Animation_speed)
turtle.hideturtle()

turtle.penup()
turtle.goto(200, - 200)

for count in range(Num_Squares):
    turtle.forward(length)
    turtle.right(turn)
    turtle.forward(length)
    turtle.right(turn)
    turtle.forward(length)
    turtle.right(turn)
    turtle.forward(length)
    turtle.right(turn)

    x = turtle.xcor() - OFFSET
    y = turtle.ycor() + OFFSET

    length = length + OFFSET

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
turtle.getscreen()._root.mainloop()