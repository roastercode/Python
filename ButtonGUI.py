#!/usr/bin/env python
# License    : GNU GPL v3 or later

""" This module is for test """

import wx


def load(event):
    file = open(FILENAME.GetValue())
    CONTENTS.SetValue(file.read())
    file.close()


def save(event):
    file = open(FILENAME.GetValue(), 'w')
    file.write(CONTENTS.GetValue())
    file.close()

APP = wx.App()
WIN = wx.Frame(None, title="Simple Editor", size=(410, 335))

BKG = wx.Panel(WIN)

LOAD_BUTTON = wx.Button(BKG, label='0pen')
LOAD_BUTTON.Bind(wx.EVT_BUTTON, load)

SAVE_BUTTON = wx.Button(BKG, label='Save')
SAVE_BUTTON.Bind(wx.EVT_BUTTON, save)

FILENAME = wx.TextCtrl(BKG)
CONTENTS = wx.TextCtrl(BKG, style=wx.TE_MULTILINE | wx.HSCROLL)

HBOX = wx.BoxSizer()
HBOX.Add(FILENAME, proportion=1, flag=wx.EXPAND)
HBOX.Add(LOAD_BUTTON, proportion=0, flag=wx.LEFT, border=5)
HBOX.Add(SAVE_BUTTON, proportion=0, flag=wx.LEFT, border=5)

VBOX = wx.BoxSizer(wx.VERTICAL)
VBOX.Add(HBOX, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
VBOX.Add(CONTENTS, proportion=1,
         flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

BKG.SetSizer(VBOX)
WIN.Show()

APP.MainLoop()
