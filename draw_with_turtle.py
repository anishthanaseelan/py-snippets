import turtle             # Allows us to use turtles
import random 
wn = turtle.Screen()      # Creates a playground for turtles
line = turtle.Turtle()    # Create a turtle, assign to alex
line.speed(10000)
wn.bgcolor("black")
line.pensize(3)
line.color ("sky blue")

def sq(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (4):
        line.forward(5*scale)          
        line.left(90)             
    if (fill):
        line.end_fill()

def tri(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (3):
        line.forward(5*scale)         
        line.left(120)
    if (fill):
        line.end_fill()

def pend(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (5):
        line.forward(5*scale) 
        line.left(72)   
    if (fill):
        line.end_fill()          
def hex(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (6):
        line.forward(5*scale)          
        line.left(60)   
    if (fill):
        line.end_fill()         
def cir(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (120):
        line.forward(.25 *scale)          
        line.left(3)         
    if (fill):
        line.end_fill()    

def egg(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    for i in range (60):
        line.forward(.25 *scale)          
        line.left(3)             
    for i in range (20):
        line.forward(.25 *scale)          
        line.left(1)             
    for i in range (60):
        line.forward(.25 *scale)          
        line.left(4)          
    for i in range (20):
        line.forward(.25 *scale)          
        line.left(1)        
    if (fill):
        line.end_fill() 

def drop(scale=1, fill=False):
    if (fill ):
        line.begin_fill()
    line.forward(.5 *scale)
    for i in range (20):
        line.left(1) 
        line.forward(.25 *scale)          
    for i in range (57):
        line.forward(.25 *scale)          
        line.left(4)          
    for i in range (24):
        line.forward(.25 *scale)          
        line.left(1)        
    if (fill):
        line.end_fill() 

shape_lst = [ sq, tri, drop, hex, pend, cir ]
color_lst = ["sky blue", "pink" , "orange", "green" , "red"]
        
def drw_spiral():
        line.color ("orange")
        for i in range (48):
                drop(scale=40)
        line.color ("sky blue")
        for i in range (48):
                drop(scale =30)
        line.color ("pink")
        for i in range (48):
                drop(scale=20)

def rand_shapes():

        for i in range(30):
                #print (random.randrange(200))
                line.penup()
                line.setx(random.randrange(-300, 300))
                line.sety(random.randrange(-300, 300))
                line.pendown()
                line.color(random.choice(color_lst))
                line.fillcolor(random.choice(color_lst))
                shape_lst[random.randrange(6)](scale=random.randrange(5, 25), fill=True)
                #sq(scale=random.randrange(30))

#drw_spiral()
#drop(scale=30)
rand_shapes()
line.getscreen().getcanvas().postscript(file='shapes.ps')

#sq(scale=10)s
#tri(scale=20)
#pend(scale=30)
#hex(scale=40)
#cir(scale=50)
#drop(scale=30)
#drop(scale=20)
#drop(scale=20)
#line.begin_fill()
#drop(scale=30)
#line.end_fill()
#line.fillcolor("yellow")

wn.mainloop()             # Wait for user to close window




