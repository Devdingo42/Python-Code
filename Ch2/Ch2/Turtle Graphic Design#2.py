import turtle
turtle.setup(640, 480)
turtle.bgcolor('blue')
turtle.fillcolor("red")
turtle.begin_fill()
turtle.setheading(67.5)
#turtle.right(80)
turtle.forward(200)
turtle.right(135)
turtle.forward(200)
turtle.right(112.5)
turtle.forward(153)
turtle.end_fill()


turtle.fillcolor('white')
turtle.begin_fill()
turtle.setheading(40)
turtle.forward(100)
turtle.right(80)
turtle.forward(105)

turtle.end_fill()

turtle.getscreen()._root.mainloop()