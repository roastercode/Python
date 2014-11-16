#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server
# Created on : Sun Nov 16 10:09:19 2014
#
# Write with Emacs-Nox
#
# References
#
# socket gethostname socket.socket.connect
#
#
# Course material
#
# Python book - Own modification
#

#
# Minimal Python Socket Server
# Socket "Information Channel"
#

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Connection from' , addr
    c.send('Welcome on board')
    c.close
