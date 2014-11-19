#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Improved Logging Server
# Created on : Wed Nov 19 19:58:20 2014
#
# Write with Emacs-Nox
#
# References
#
# twisted reactor SimpleLogger
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
#

#
# Improved Logging Server
# Socket "Information Channel"
# Works with py3socket-client.py
# 

from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):

    def connectionMade(self):
        print ('Got connection from'), self.transport.client

    def connectionLost(self, reason):
        print ('disconnect'), self.transport.client

    def lineReceived(self, line):
        print (line)

factory = Factory()
factory.protocol = SimpleLogger


reactor.listenTCP(1234, factory)
reactor.run()
