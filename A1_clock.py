#draw a clock displaying time 9.15.00

import turtle

turtle.penup()
turtle.goto(0,-250)
turtle.pendown()
turtle.circle(250)

turtle.write("6", move=False, align = 'center', font= ("Arial", 20, "normal"))
turtle.penup()
turtle.goto(240,0)
turtle.pendown()
turtle.write("3", move=False, align = 'center', font= ("Arial", 20, "normal"))
turtle.penup()
turtle.goto(-240,0)
turtle.pendown()
turtle.write("9", move=False, align = 'center', font= ("Arial", 20, "normal"))
turtle.penup()
turtle.goto(0,230)
turtle.pendown()
turtle.write("12", move=False, align = 'center', font= ("Arial", 20, "normal"))


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.dot(5)
turtle.pencolor("red")
turtle.back(150)
turtle.forward(350)
turtle.back(200)
turtle.left(90)
turtle.forward(225)
turtle.penup()

turtle.goto(-5,-280)
turtle.pencolor("black")
turtle.write("9:15:00", align='center', font = ("Arial",20,"normal"))



