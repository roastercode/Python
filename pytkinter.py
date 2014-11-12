#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Box
# Created on : Wed Nov 12 19:57:49 2014
#
# Write with Emacs-Nox
#
# References
#
# python2 env
# wx, tkinter
#
# Course material
#
# MOOC INRIA box
#

from Tkinter import *

def hello(): print 'Hello, world'
win = Tk() # the window
win.title('Tkinter! ')
win.geometry('250x100') # size of the window

btn = Button(win, text='Tkinter! ', command=tkinter)
btn.pack(expand=YES, fill=BOTH)

mainloop()
