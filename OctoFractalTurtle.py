#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Octo Fractal Turtle
# Created on : Sat Nov 8 14:25:00 2014
#
# Write with Emacs-Nox
#
# References
#
# python2 env
# Fractal Turtle
#
# Course material
#
# MOOC INRIA Turtle
#

import turtle

def fractal_side(length, fractal):
    if fractal == 0:
        turtle.forward(length)
    else:
        length8 = length / 8.
        fractal_side(length8, fractal-1)
        turtle.left(45)
        fractal_side(length8, fractal-1)
        turtle.right(45)
        fractal_side(length8, fractal-1)
        turtle.left(45)
        fractal_side(length8, fractal-1)
        turtle.right(45)
        fractal_side(length8, fractal-1)
        turtle.left(45)
        fractal_side(length8, fractal-1)
        turtle.right(45)
        fractal_side(length8, fractal-1)
        turtle.left(45)
        fractal_side(length8, fractal-1)
        turtle.right(45)
        
turtle.reset()
turtle.speed('fastest')
fractal_triangle(400, 3)
turtle.exitonclick()
