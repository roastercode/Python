#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server Select
# Created on : Tue Nov 18 06:28:58 2014
#
# Write with Emacs-Nox
#
# References
#
# socket gethostname socket.socket.connect
# select
#
# Course material
#
# Python book - Own modification - Python Documentation
#

#
# Minimal Python Socket Server Select
# Socket "Information Channel"
# 

import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]

while True:
    rs, ws, es = select.select(inputs, [],[])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print ('Connection from'), addr
            inputs.append(c)

        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print ('disconnect'), r.getpeername(),
                inputs.remove(r)
            else:
                print (data)
