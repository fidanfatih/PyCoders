from tkinter import *

def draw_triangle(a,b,c):
    # determine corner points of triangle with sides a, b, c
    A=(0,0)
    B=(c,0)
    hc=(2 * (a ** 2 * b ** 2+b ** 2 * c ** 2+c ** 2 * a ** 2)-(a ** 4+b ** 4+c ** 4)) ** 0.5 / (2. * c)
    dx=(b ** 2-hc ** 2) ** 0.5
    if abs ((c-dx) ** 2+hc ** 2-a ** 2) > 0.01: dx=-dx  # dx has two solutions
    C=(dx,hc)

    # move away from topleft, scale up a bit, convert to int
    coords=[int ((x+1) * 75) for x in A+B+C]

    # draw using Tkinter
    root=Tk ()
    canvas=Canvas (root,width = 1000,height = 1000)
    canvas.create_polygon (*coords)
    canvas.pack ()
    root.mainloop ()


def draw_rectangle(a,b):
    # determine corner points of triangle with sides a, b, c
    A,B,C,D=(0,0),(a,0),(a,b),(0,b)

    # move away from topleft, scale up a bit, convert to int
    coords=[int ((x+1) * 75) for x in A+B+C+D]

    # draw using Tkinter
    root=Tk ()
    canvas=Canvas (root,width = 1000,height = 1000)
    canvas.create_polygon (*coords)
    canvas.pack ()
    root.mainloop ()


def draw_circle(r):
    x,y=(300,300)  # center coordinates

    x0,y0=x-20 * r,y-20 * r
    x1,y1=x+20 * r,y+20 * r

    # draw using Tkinter
    root=Tk ()
    canvas=Canvas (root,width = 1000,height = 1000)
    canvas.create_oval (x0,y0,x1,y1,fill = "black")
    canvas.pack ()
    root.mainloop ()

triangle_sides = [3,4,5]
rectangle_sides = [3,4]
circle_radius = 5

draw_triangle (*triangle_sides)
draw_rectangle (*rectangle_sides)
draw_circle (circle_radius)