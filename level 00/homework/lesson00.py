from turtle import *
#we want to paint a house

#step 1: draw a square
speed(15)
width(7)
color("purple")
forward(200)
left(90)  

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#drawing a door

forward(70)
color("yellow")
left(90)
forward(120)
right(90)
forward(60)   #height of door
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#begin of window
color("purple")
penup()
goto(150,150)
pendown()
left(30)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
right(180)
forward(12)
right(90)
forward(50)
penup()
goto(150,150)
pendown()
forward(25)
left(90)
forward(25)

#second window

color("purple")
penup()
goto(0,0)
pendown()
left(90)
forward(150)
right(90)
forward(5)
color("white")
forward(20)
color("purple")
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(90)
forward(12.5)
right(90)
forward(50)
left(90)
forward(12.5)
left(90)
forward(25)
left(90)
forward(25)

#house is finished














exitonclick()