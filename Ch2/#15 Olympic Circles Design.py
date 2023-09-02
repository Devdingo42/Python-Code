import turtle
 
#Ring size
turtle.pensize(1)
 
#First ring
turtle.color("black")
turtle.penup()
turtle.goto(-117, -60)
turtle.pendown()
turtle.circle(45)

#Second Ring
turtle.color("black")
turtle.penup()
turtle.goto(0, -56)
turtle.pendown()
turtle.circle(45)
 
#Third Ring
turtle.color("black")
turtle.penup()
turtle.goto(115, -55)
turtle.pendown()
turtle.circle(45)
 
#Fourth Ring
turtle.color("black")
turtle.penup()
turtle.goto(-60, -80)
turtle.pendown()
turtle.circle(45)
 
#Fifth Ring 
turtle.color("black")
turtle.penup()
turtle.goto(70, -75)
turtle.pendown()
turtle.circle(45)

turtle.getscreen()._root.mainloop()