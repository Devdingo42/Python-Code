import turtle

#Pensize and Hidden ability!!!
turtle.pensize(2)
turtle.hideturtle()

#First move
turtle.color('black')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.dot(size = 16)
turtle.left(45)
turtle.forward(200)
turtle.dot(size = 16)

#Second move
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.dot(size = 16)

#Thrid Move
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.dot(size = 16)

#Fourth Move
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(200)
turtle.dot(size = 16)
turtle.penup()

#Fith Move
turtle.pendown()
turtle.right(135)
turtle.forward(25)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(35)

#Sixth Move
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.forward(25)
turtle.pendown()
turtle.forward(35)

#7th Move
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(35)

#8th move
turtle.pendown()
turtle.right(90)
turtle.forward(25)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.forward(25)
turtle.pendown()
turtle.forward(35)

turtle.end_fill()
turtle.getscreen()._root.mainloop()