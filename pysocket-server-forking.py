#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Forking Socket Server
# Created on : Mon Nov 17 13:37:22 2014
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
# Duplication of server by forking
#

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Connection from', addr
        self.wfile.write('Welcome on board!')

server = Server(('', 1234), Handler)
server.serve_forever()
