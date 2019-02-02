'''
Turtle: two chessboards) Write a program that displays two chessboards, as shown
in Figure. Your program should define at least the following function:
# Draw one chessboard whose upper-left corner is at # (startx, starty) and
bottom-right corner is at (endx, endy) 
def drawChessboard(startx, endx, starty, endy):
'''

import turtle

screen = turtle.Screen()
screen.screensize(500,500)
turtle.speed(10)

def drawSquare(length):    
    for sides in range (4):
        turtle.forward(length)
        turtle.rt(90)

def drawChessboard(startx, starty, endx, endy):
    length_of_board = endx - startx
    height_of_board = starty - endy
    #verify if we can get a perfect square from the given dimensions if not
    #adjust square to the shortest length/breadth of the rectangle
    if(height_of_board <= length_of_board):
        length_of_eachsquare = height_of_board/8
    elif (height_of_board >= length_of_board):
        length_of_eachsquare = length_of_board/8
    #varible that controls the color of the square    
    color_flag = True
    x=startx
    y=starty
    for vertical in range(8):     
        for horizantal in range (0,8):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            if color_flag: #white square
                drawSquare(length_of_eachsquare)
                color_flag= False
            else: #black square
                turtle.color("black","black")
                turtle.begin_fill()
                drawSquare(length_of_eachsquare)
                turtle.end_fill()
                color_flag= True
            x=x+length_of_eachsquare
        #going to the next line on the baord
        x=startx
        y=y-length_of_eachsquare
        color_flag = not color_flag  
    

#main program

drawChessboard(-250,250,0,0)

drawChessboard( 10,250,260,0)


        
                
            
