#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Python Box
# Created on : Thu Nov 13 12:01:03 2014
#
# Write with Emacs-Nox
#
# Python3 Client
#

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connection to hostname on the port.
s.connect((host, port))

# receive no more than 1024 bytes
msg = s.recv(1024)

s.close()

print (msg.decode('ascii'))
