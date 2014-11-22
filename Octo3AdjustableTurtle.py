#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Octo Adjustable Turtle
# Created on : Sat Nov 8 14:30:20 2014
#
# Write with Emacs-Nox
#
#
# References
#
# python2 env
# octo turtle
#
# Course material
#
# MOOC INRIA Turtle
#

import turtle


def left_triangle(length):
        for i in range(3):
            turtle.forward(length)
            turtle.left(110)


def fractal_side(length, fractal, proportions):
    if fractal == 0:
        turtle.forward(length)
    else:
        [l1, l2, l3, l4, l5, l6, l7, l8] = [p*length for p in proportions]
        fractal_side(l1, fractal-1, proportions)
        turtle.right(80)
        fractal_side(l2, fractal-1, proportions)
        turtle.left(110)
        fractal_side(l3, fractal-1, proportions)
        turtle.right(80)
        fractal_side(l4, fractal-1, proportions)
        turtle.left(110)
        fractal_side(l5, fractal-1, proportions)
        turtle.right(80)
        fractal_side(l6, fractal-1, proportions)
        turtle.left(110)
        fractal_side(l7, fractal-1, proportions)
        turtle.right(80)
        fractal_side(l8, fractal-1, proportions)


def fractal_triangle(length, fractal, proportions):
        for i in range(3):
            fractal_side(length, fractal, proportions)
            turtle.left(110)


turtle.reset()
turtle.speed(10)
fractal_triangle(400, 3, (.3, .3, .3, .3, .3, .3, .3, .3))
turtle.exitonclick()
