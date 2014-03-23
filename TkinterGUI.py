#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : aurelien desbrieres
# Mail      : aurelien@hackers.guru
# Project   : TkinterGUI

from Tkinter import *
def hello(): print 'Hello, world'
win = Tk() # Tkinter's 'main window'
win.title('Hello, Tkinter! ')
win.geometry('200x100') # Size 200, 100

btn = Button(win, text='Hello ', command=hello)
btn.pack(expand=YES, fill=BOTH)

mainloop()
