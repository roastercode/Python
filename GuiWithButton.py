#!/usr/bin/env python3
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : GuiWithButton
# Created on : 
#
#
# Write with Emacs-Nox
#
# References
#
# python3 env
#
#
# Course material
#

import wx
app = wx.App()
win = wx.Frame(None)
btn = wx.Button(win)
win.Show()
app.MainLoop()
