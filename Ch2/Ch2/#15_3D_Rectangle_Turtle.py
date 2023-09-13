import turtle 

#First Part
turtle.hideturtle()
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)

#Second Part
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)

#Third Part
turtle.setheading(315)
turtle.forward(212)
turtle.setheading(180)
turtle.forward(75)
turtle.setheading(135)
turtle.forward(105)

#Last Part
turtle.right(45)
turtle.forward(75)
turtle.right(90)
turtle.forward(75)
turtle.setheading(315)
turtle.forward(105)
turtle.end_fill()

turtle.getscreen()._root.mainloop()