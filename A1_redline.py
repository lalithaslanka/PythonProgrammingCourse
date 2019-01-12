#draw a redline connectibng coordinates

import turtle

turtle.penup()
turtle.goto(-39,48)
p1 = turtle.pos()
turtle.write(p1, move = False, align='left')
turtle.pencolor("red")
turtle.pendown()
turtle.goto(50,-50)
p2 = turtle.pos()
turtle.pencolor("black")
turtle.write(p2, move = False, align = 'left')
             
