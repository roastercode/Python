#!/usr/bin/python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Square
# Created on : Wed Jan 31 2018
# Modified   :
# Write with Emacs-Nox
#
# Pylint verified 10.00
""" Python experimentations """

# Python3 test envirronement
# If you are not able to print that square on execution,
# your envirronement is just crap
from __future__ import print_function
TEST = "┌─┐"
TSET = "└─┘"
print(TEST)
print(TSET)

## Square draw & Perimeter calculus with its algorithm

# REQUEST : L
# SAVE L AS A DATA
# REQUEST : W
# SAVE L AS A DATA
# PRINT L LINE
# BECAUSE BASH DESIGN DOES NOT RESPECT VISUAL REALITY, IMPROVE DESIGN BY X2 THE LENGHT
# PRINT W LINE WITH THE SPACE OF L-2
# PRINT L LINE TO CLOSE THE SQUARE/RECTANGLE
# USE L AND W TO CALCULATE PERIMETER
# PRINT PERIMETER BELOW THE SQUARE/RECTANGLE

# Variable definition
LENGHT = input('Give the lenght: ')
WIDTH = input('Give the with: ')

# Drawing the stuff
print('┌' + '─' * 2 * LENGHT + '┐')
DESIGN = LENGHT + 4
print(('│' + ' ' * DESIGN + '│\n') * WIDTH + ('└' + '─' * 2 * LENGHT + '┘'))

# Print the perimeter
PERIMETER = (LENGHT*WIDTH)
print(PERIMETER)
