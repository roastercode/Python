#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Twisted Server
# Created on : Wed Nov 19 09:06:43 2014
#
# Write with Emacs-Nox
#
# References
#
# twisted reactor
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
#

#
# Minimal Python Twisted Server
# Socket "Information Channel"
# Works with py3socket-client.py
# 

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):

    def connectionMade(self):
        print ('Got connection from'), self.transport.client

    def connectionLost(self, reason):
        print ('disconnected'), self.transport.client

    def dataReceived(self, data):
        print (data)

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()
