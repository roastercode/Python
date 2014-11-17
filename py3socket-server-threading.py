#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Threading Socket Server
# Created on : Mon Nov 17 14:39:10 2014
#
# Write with Emacs-Nox
#
# References
#
# socket gethostname socket.socket.connect
# TCPServer ForkingMixIn StreamRequestHandler
#
# Course material
#
# Python book - Own modification
#

#
# Minimal Python Socket Server
# Socket "Information Channel"
# Synchronisation of server by threading
#

import socketserver

from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print ('Connection from'), addr
        s = 'Welcome on board!'
        self.wfile.write(bytes(s, 'UTF-8'))

server = Server(('', 1234), Handler)
server.serve_forever() 
