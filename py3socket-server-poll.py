#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server Poll
# Created on : Tue Nov 18 07:51:48 2014
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
# Minimal Python Socket Server Poll
# Socket "Information Channel"
# 

import socket, select

s = socket.socket()

host = socket.gethostname()
port = 1235
s.bind((host, port))

fdmap = {s.fileno(): s}

s.listen(5)
p = select.poll()
p.register(s)
while True:
    events = p.poll()
    for fd, event in events:
        if fd in fdmap:
            c, addr = s.accept()
            print ('Connection from'), addr
            p.register(c)
            fdmap[c.fileno()] = c
        elif event & select.POLLIN:
            data = fdmap[fd].recv(1024)
            if not data: # No data -- connection closed
                print ('disconnect'), fdmap[fd].getpeername(),
                p.unregister(fd)
                del fdmap[fd]
            else:
                print (data)
