from turtle import *
from colorsys import *
bgcolor("black")
tracer(0)
pensize(3)
h=0
for i in range(180):
    c=hsv_to_rgb(h,1,1)
    h+=0.007
    pencolor(c)
    begin_fill()
    lt(105)
    fd(210-i)
    circle(-40,-150)
    fd(210-i)
    circle(-30,-150)
    end_fill()
    done()
