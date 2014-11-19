#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# License    : GNU GPL v3 or later
# Author     : Aurélien DESBRIERES
# Mail       : aurelien@hackers.camp
# Project    : Tidy
# Created on : 
#
# Write with Emacs-Nox
#
# References
#
# subprocess Popen PIPE
#
# Course material
#
# Python books - Own modification - Python Documentation - WWW
#
#


from subprocess import Popen, PIPE


text = open('wild.html').read()
tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)

t = 'tidy'
tidy.stdin.write(bytes(t, 'UTF-8'))
tidy.stdin.close()

print (tidy.stdout.read())
