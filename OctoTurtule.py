#!usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : OctoTurtle
# Created on : Thu Nov 6 17:47:39 2014
#
#
# Course material
#
# MOOC INRIA PYTHON
#
# 
# Draw octagon

# import turtle module
import turtle

# define function that draw a number of side (range)
# with an angle on make turn the turtle


def octo(length):
    "have the turtle draw a square of side <length>"
    for side in range(8):
        turtle.forward(length)
        turtle.left(45)

# Start the turtle on 0

turtle.reset()

# define the lenght of each range

octo(100)


# stand for the user mouse clic to exit

turtle.exitonclick()

