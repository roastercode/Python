#!/usr/bin/env python
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Javax Box
# Created on : Sat Nov 15 15:22:44 2014
#
# Write with Emacs-Nox
#
# References
#
#
# Course material
#
# Python box made of Javax
#

from javax.Swing import *
import sys

def hello(event): print Hello, world!
btn = JButton('Hello')
btn.actionPerformed = hello

win = JFrame('Hello, Swing!')
win.contentPane.add(btn)

def closeHandler(event): sys.exit()
win.windowClosing = closeHandler

btn.size = win.size = 200, 100
win.show()
