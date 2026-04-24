#Program

#Uses the function file and imports all the functions
from Function import *
#import turtle
import turtle
#variable to allow drawing on the screen.
mug = turtle.Turtle()
#Pen goes up
mug.penup()
#Speed to draw the image
mug.speed(0)
#variable to allow user input on the screen.
screen = turtle.Screen()
#Titles the turlte page
screen.title("GIFT MUG IMAGE")
#User is prompted to enter the background color.
background = turtle.textinput("background Color","Color")
#User is prompted to enter the recipient's name.
name = turtle.textinput("Recipient's name","Name")
#User is prompted to enter the recipient's age.
age = turtle.textinput("Recipient's age","Age")
#User is prompted to enter the mug color.
mug_color = turtle.textinput("Mug color","Color")
#User is prompted to enter the saucer plate color.
plate_color = turtle.textinput("Saucer plate color", "Color")
#User is prompted to enter the font type.
font_type = turtle.textinput("Message font type","Font Type")
#Change the background color using the user's input
turtle.bgcolor(background)
#Pen width is 10.
mug.width(10)
#Call the function to create the base.
create_base(mug_color,mug)
#Call the function to create the handle.
draw_handle(mug_color,mug)
#Call the function to create the saucer plate.
create_saucer(plate_color,mug)
#Call the function that displays the text.
display_message(name,age,font_type,mug)
#Hides the turtle from the drawing
mug.hideturtle()
#turtle done
turtle.done()

