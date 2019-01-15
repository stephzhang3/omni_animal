import _tkinter
import Tkinter as tk
from turtle import *
import turtle
import math

def draw_eye():
  pd()
  for x in xrange(0, 360):
    fd(x)
    rt(x)
  pu()

def draw_wave(size, heading):
  if size <= 0:
    return
  else:
    pd()
    fd(size)
    pu()
    x = xcor()
    y = ycor()
    lt(87)
    draw_wave(size/2, heading+87)
    goto(x,y)
    setheading(heading-15)
    factor = int(size/10)
    if factor < 1:
      factor = 1
    draw_wave(size-factor, heading-15)

def save_img(filename):
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file=filename)

def main():
  # Set turtle speed/pen/location settings
  clearscreen()
  setup(width=1.0, height=1.0, startx=None, starty=None)
  pu()
  goto(-400,-400)
  hideturtle()
  turtle.tracer(0, 0)
  turtle.speed(10)

  #draw_eye() # Uncomment this to generate eye file instead of wave
  setheading(90)
  draw_wave(100, 90)
  save_img("wave.eps")

main()
