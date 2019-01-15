from turtle import *
import _tkinter
import Tkinter as tk
from turtle import *
import turtle
import math

turtle.hideturtle()

#exitonclick()
def save_img(filename):
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file=filename)

speed(0) # sets the speed of drawing to 0, which is the fastest
pencolor('black') # sets the color of the pen/lines to white
bgcolor('red') # sets the color of the background/canvas to black

up() # lifts up the pen, so no lines are drawn

#note fd() means move forward, bk() means move back
# rt() or lt() means tilt right by a certain angle

rt(45)
fd(90)
rt(135)

down() # sets down the pen, so that turtle can draw

def star():
    x = 0 # creates a variable x with value
    while x < 16: # while the value of x is lesser than 120,
                    #continuously do this:
        for i in range (0,4):
            fd(100)
            rt(100)


        rt(30.1111)
        x = x+1 # adds 1 to the value of x,
                # so that it is closer to 120 after every loop
    save_img("star.eps")

def glass():
    x = 0
    while x < 12: # while the value of x is lesser than 120,
                    #continuously do this:
        for i in range (0,4):
            fd(100)
            rt(120)


        rt(30)
        x = x+1 # adds 1 to the value of x,
                # so that it is closer to 120 after every loop
    save_img("glass.eps")

#star()
glass()
