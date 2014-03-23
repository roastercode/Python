#!/usr/bin python
# -*- coding: utf-8 -*-
# License   : GNU GPL v3 or later
# Author    : aurelien desbrieres
# Mail      : aurelien@hackers.guru
# Project   : ButtonInformation

import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor")
loadButton = wx.Button(win, label='0pen')
saveButton = wx.Button(win, label='Save')

win.Show()
app.MainLoop()
