#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Octo Multi Turtle
# Created on : Sat Nov 22 07:49:46 2014
#
# Write with Emacs-Nox
#
# References
#
# python3 env
# octo turtle
#
# Course material
#
# MOOC INRIA Turtle - WWW - pydoc
#


# we need the turtle module
import turtle

# avoid calling range for each square
sides = ['east', 'north-east', 'north', 'south-west', 'west', 'south-est', 'south', 'south-west']

def octo(the_turtle, length):
    "have the turtle draw a octo of side <length>"
    for side in sides:
        the_turtle.forward(length)
        the_turtle.left(45)

# initialize
window = turtle.Screen()
window.title("Caroline, Chloe && Bob")

# create first turtle
caroline = turtle.Turtle()
caroline.color("hotpink")
caroline.reset()

# second turtle
chloe = turtle.Turtle()
chloe.color("lightgreen")
chloe.reset()

# create third turtle
bob = turtle.Turtle()
bob.color("blue")
bob.reset()

# alternate : turtle, twist and octo size
contexts = ((caroline, 15, 100, ),
            (chloe, 60, 30 ),
            (bob, 40, 60 ),
           )
# initialize alternating contexts
cycle = len(contexts)
counter = -1

# the callback triggered when a user clicks in x,y
def clicked(x, y):
    global counter
    counter += 1
    # alternate between the various contexts
    (turtle, twist, size) = contexts[counter % cycle]
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(twist)
    octo(turtle, size)

# arm callback
turtle.onscreenclick(clicked)

# user can quit by typing 'q'
turtle.onkey(turtle.bye, 'q')
turtle.listen()

# read & dispatch events
turtle.mainloop()
