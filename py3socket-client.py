#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server
# Created on : Mon Nov 17 18:35:19 2014
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
#    $ python3 py3socket-server.py
# load from another terminal
#    $ python3 py3socket-client.py
#

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
s.recv(1024)

print ("Welcome on board!")
