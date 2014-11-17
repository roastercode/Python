#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Socket Server
# Created on : Mon Nov 17 17:36:27 2014
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
# Python3 documentation - Own modification
#

#
# Minimal Python Socket Client
# Socket "Information Channel"
#

# This python3 client works with the Python2 solution of the
# pysocket-server.py write
#
# load from a terminal
#    $ python pysocket-server.py
# load from another terminal
#    $ python pysocket-client.py
#

import socket
import sys

HOST, PORT = "localhost", 1234
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
sock.sendall(bytes(data + "\n", "utf-8"))

received = str(sock.recv(1024), "utf-8")

sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
