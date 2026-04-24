#Turtle is imported
import turtle

#function to create mug (excluding handle)
#takes the variable mug color as a parameter.
def create_base(color,mug):    
    #Pen goes up
    mug.up()
    #Pen goes to position (-200,-200)
    mug.goto(-200,-200)
    #Pen goes down
    mug.down()
    #Fill the shape with the color
    mug.fillcolor(color)
    #Begins the fill
    mug.begin_fill()
    #Loops two times
    for i in range(2):
        #Moves forward 400
        mug.forward(400)
        #Turns right 90 degrees
        mug.left(90)
        #Moves forward 450
        mug.forward(450)
        #Turns left 90 degrees
        mug.left(90)
    #Ends the fill
    mug.end_fill()
    
#Function to create the mug handle
#takes the variable mug color as a parameter.
def draw_handle(color,mug):
    #Pen goes up
    mug.up()
    #Goes to position (-200,-50)
    mug.goto(-200,-50)
    #Turn 90 degrees to the left
    mug.left(180)
    #Puts the color in the handle
    mug.fillcolor(color)
    #Starts filling the shape with the color
    mug.begin_fill()
    #Pen goes down
    mug.down()
    #Move forward 100
    mug.forward(100)
    #turn 90 degrees
    mug.right(90)
    #Move forward 150
    mug.forward(150)
    #Turn 90 degrees to the right
    mug.right(90)
    #Move forward 100
    mug.forward(100)
    #Pen up
    mug.up()
    #Turn 90 degrees
    mug.right(90)
    #move forward 150
    mug.forward(120)
    #Turn right 90 degrees
    mug.right(90)
    #Pen down
    mug.down()
    #MOve forward 70
    mug.forward(70)
    #Move right 90 degrees
    mug.right(90)
    #Move forward 90
    mug.forward(90)
    #Turn right 90 degree
    mug.right(90)
    #Move forward 70
    mug.forward(70)
    #Stops the fill
    mug.end_fill()

#function to create the saucer plate
#Takes the variable saucer plate color as a parameter
def create_saucer(color,mug):
    #pen goes up
    mug.up()
    #Turn 90 degrees to the right
    mug.right(90)
    #Move forward
    mug.forward(270)
    #Color variable used to color shape
    mug.fillcolor(color)
    #Begins coloring the shape
    mug.begin_fill()
    #Pen goes down
    mug.down()
    #Turns 90 degrees to the right
    mug.right(90)
    #Pen goes forward 150
    mug.forward(150)
    #Turns 90 degrees to the left
    mug.left(90)
    #Moves forward 100
    mug.forward(100)
    #Turns left 90 degrees
    mug.left(90)
    #Moves forward 600
    mug.forward(700)
    #Turns left 90 degrees
    mug.left(90)
    #Moves forward 100
    mug.forward(100)
    #Turns left 90 degrees
    mug.left(90)
    #Moves forward 550
    mug.forward(550)
    #Stops coloring the shape
    mug.end_fill()
    
#function to create the header and message on the mug
#Takes in the recipient's name and age and the font style.
def display_message(name,age,font,mug):
    #Pen goes up
    mug.up()
    #Go to position (0,280)
    mug.goto(0,280)
    #Pen goes down
    mug.down()
    #Message of variable name is displayed, center of the page, variable font type, font size 46, bold.
    mug.write(f"{name}'s GIFT", align="center",font=(f"{font}",46,"normal"))
    #Pen goes up
    mug.up()
    #Change the width to 5
    mug.width(5)
    #Goes to position (0,180)
    mug.goto(0,180)
    #Pen goes down
    mug.down()
    #Message Happy is displayed, center of the page, variable font type, font size 32, bold.
    mug.write("H  A  P  P  Y", align="center", font=(f"{font}",32,"bold"))
    #Pen goes up
    mug.up()
    #Go to position (0,100)
    mug.goto(0,100)
    #Pen goes down
    mug.down()
    #Message age variable is displayed, center of the page, variable font type, font size 35, bold.
    mug.write(f"{age} t h",align="center",font=(f"{font}",35,"bold"))
    #Pen goes up
    mug.up()
    #Goes to position (0,10)
    mug.goto(0,10)
    #Pen goes down
    mug.down()
    #Message Birthday is displayed, center of the page, variable font type, font size 32, bold.
    mug.write("B  I  R  T  H  D  A  Y", align="center", font=(f"{font}",32,"bold"))
    #Turns 180 degrees to the right
    mug.right(180)
    #Pen goes up
    mug.up()
    #if there are more than 6 characters, this runs.
    if len(name)<=6:
        #Goes to position (-80,-100)
        mug.goto(-80,-100)
        #Pen goes down
        mug.down()
        #For each character in the variable.
        for x in name:
            #Writes the character with the font type variable, font size 35 and in bold.
            mug.write(f"{x} ",align="center",font=(f"{font}",35,"bold"))
            #Pen goes up
            mug.up()
            #Goes forward 50
            mug.forward(50)
            #Pen goes down
            mug.down()
    #If bigger than or equal to 6 characters and less than 8 characters, this runs.
    elif len(name)>6 and len(name)<=8:
        #Goes to position (-120,-100)
        mug.goto(-120,-100)
        #For each character in the name variable
        for x in name:
            #Writes the character with the font type variable,aligned to the center, font size 32 and in bold.
            mug.write(f"{x} ",align="center",font=(f"{font}",32,"bold"))
            #Pen goes up
            mug.up()
            #Pen goes forward 40
            mug.forward(40)
            #Pen goes down
            mug.down()
    
    #If bigger than 8 characters, this runs.
    else:
        #Pen goes to position (-170,-100)
        mug.goto(-170,-100)
        #For each character in the name variable
        for x in name:
            #Writes the character with the font type variable,aligned to the center, font size 30 and in bold.
            mug.write(f"{x} ",align="center",font=(f"{font}",30,"bold"))
            #Pen goes up
            mug.up()
            #Pen goes forward 40
            mug.forward(40)
            #Pen goes down
            mug.down()
    
 





    
