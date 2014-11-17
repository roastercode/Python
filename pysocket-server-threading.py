#!/usr/bin/env python2
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


from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Connection from', addr
        self.wfile.write('Welcome on board!')

server = Server(('', 1234), Handler)
server.serve_forever()
