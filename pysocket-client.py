#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server
# Created on : Sun Nov 16 11:46:34 2014
#
# Write with Emacs-Nox
#
# References
#
# socket gethostname socket.socket socket.socket.connect
#
#
# Course material
#
# Python book - Own modification
#

#
# Minimal Python Socket Client
# Socket "Information Channel"
#

# load from a terminal
#    $ python pysocket-server.py
# load from another terminal
#    $ python pysocket-client.py
#

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print s.recv(1024)
