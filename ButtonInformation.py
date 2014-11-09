#!/usr/bin/env python3
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : ButtonInformation.py
# Created on : Mon Nov 3 19:50:58 2014
#
# Write with Emacs-Nox
#
# References
#
# python3 env
#
#
#
#


import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor")
loadButton = wx.Button(win, label='0pen')
saveButton = wx.Button(win, label='Save')

win.Show()
app.MainLoop()
