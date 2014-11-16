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
# StreamRequestHandler TCPServer
#
# Course material
#
# Python book + Own modification
#

#
# Minimal Python Socket Server that close the connection
# when it has been handled
#
# Socket "Information Channel"
#

from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Connection' , addr
        self.wfile.write('Welcome on board!')

server = TCPServer(('', 1234), Handler)
server.serve_forever()
