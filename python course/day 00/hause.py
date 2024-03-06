from turtle import *

#we wont to paint a house

#step 1: drew a squere

shape("turtle")
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

#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

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

#drew a window

color("purple")
left(30)
forward(40)
color("blue")
begin_fill()
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

penup()
goto(200,100)
pendown()

color("blue")
begin_fill()
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
end_fill()

exitonclick()